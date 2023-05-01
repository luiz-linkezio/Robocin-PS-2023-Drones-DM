from __future__ import print_function
import time
from dronekit import connect, VehicleMode, LocationGlobalRelative, mavutil

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

# Usando a def de movimentação do drone        
send_ned_velocity(vehicle,1.53,0,0,1) #(veículo,x,y,z,tempo)
