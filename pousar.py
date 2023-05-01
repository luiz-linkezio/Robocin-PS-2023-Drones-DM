from __future__ import print_function
import time
from dronekit import connect, VehicleMode, LocationGlobalRelative

# Cód de conexão do veículo
connection_string = "127.0.0.1:14550"

# Conectando ao veículo
vehicle = connect(connection_string, wait_ready=True)

# Mudando modo do veículo para LAND e desarmando
vehicle.mode = VehicleMode("LAND")
vehicle.armed = False
