
from fse103 import FSE103

sensor = FSE103("/dev/ttyACM0")

while True:
    sensor.read()
    print(sensor.serialport.in_waiting, sensor.timestamp, sensor.force_z, sensor.raw_z)