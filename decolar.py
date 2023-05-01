from __future__ import print_function
import time
from dronekit import connect, VehicleMode, LocationGlobalRelative, mavutil



# Cód de conexão do veículo
connection_string = "127.0.0.1:14550"

# Conectando ao veículo
vehicle = connect(connection_string, wait_ready=True)

# Esperando
while not vehicle.is_armable:
    time.sleep(1)

# Mudando para o modo guided e se armando
vehicle.mode = VehicleMode("GUIDED") 
vehicle.armed = True

# Esperar veículo se armar
while not vehicle.armed:
    time.sleep(1)

# Decolagem para a altura 0.8
vehicle.simple_takeoff(0.8)

time.sleep(5)
