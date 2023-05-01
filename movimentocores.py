from __future__ import print_function
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np
from dronekit import connect, VehicleMode, LocationGlobalRelative, mavutil
import time

# Cód de conexão do veículo
connection_string = "127.0.0.1:14550"

# Conectando ao veículo
vehicle = connect(connection_string, wait_ready=True)

# Def de movimentação que peguei no site oficial que contém a documentação do dronekit
def send_ned_velocity(vehicle, velocity_x, velocity_y, velocity_z, duration):
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
        0,       # time_boot_ms (not used)
        0, 0,    # target system, target component
        mavutil.mavlink.MAV_FRAME_LOCAL_NED, # frame
        0b0000111111000111, # type_mask (only speeds enabled)
        0, 0, 0, # x, y, z positions (not used)
        velocity_x, velocity_y, velocity_z, # x, y, z velocity in m/s
        0, 0, 0, # x, y, z acceleration (not supported yet, ignored in GCS_Mavlink)
        0, 0)    # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink)

    # send command to vehicle on 1 Hz cycle
    for x in range(0, duration):
        vehicle.send_mavlink(msg)
        time.sleep(1)

class ImageSubscriber(Node):
    def __init__(self):
        super().__init__('image_subscriber')
        self.subscription = self.create_subscription(
            Image,
            'camera/image_raw',  # substitua este tópico pelo tópico que você está usando para a imagem
            self.listener_callback,
            10)
        self.bridge = CvBridge()
        self.central_pixel = None
        
        self.final = False
			
    def listener_callback(self, data):
        cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        cv2.imshow("Image window", cv_image)
        
        # Obtém as dimensões da imagem
        height, width, channels = cv_image.shape

        # Obtém o pixel central
        if self.central_pixel is None:
            self.central_pixel = (int(width/2), int(height/2))
        else:
            # Encontra o pixel central no novo quadro
            self.central_pixel = (int(width/2), int(height/2))

        
        # Obtém os valores RGB do pixel central
        x, y = self.central_pixel
        b, g, r = cv_image[y, x]
        
        
        if r == 218 and b == 218 and g == 218:
            send_ned_velocity(vehicle,0.2,0.1,0,1) 
        
        elif r > 200 and b > 200 and g < 30:        
            send_ned_velocity(vehicle,0.2,0,0,1)   
        elif r > (1.5*b) and r > (1.5*g):
            send_ned_velocity(vehicle,0,0.2,0,1)
            self.final = True
        elif g > (1.5*b) and g > (1.5*r):
            if self.final == False:
                send_ned_velocity(vehicle,-0.2,0,0,1)
            else:
                vehicle.mode = VehicleMode("LAND")
                vehicle.armed = False
        elif b > (1.5*r) and b > (1.5*g):
            send_ned_velocity(vehicle,0,-0.2,0,1)     
        
        print(f"Pixel ({x}, {y}): R={r}, G={g}, B={b}")
                
        cv2.waitKey(1)



def main(args=None):
    rclpy.init(args=args)
    image_subscriber = ImageSubscriber()
    while rclpy.ok():  # Loop que só se quebra quando o drone pousa
        rclpy.spin_once(image_subscriber)
        if vehicle.mode.name == "LAND":
            break
    image_subscriber.destroy_node()
    rclpy.shutdown()
    time.sleep(10)


if __name__ == '__main__':
    main()

