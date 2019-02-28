
from fse103 import FSE103

sensor = FSE103("/dev/ttyACM0")

while True:
    sensor.read()
    print(sensor.timestamp, sensor.force_x, sensor.force_y, sensor.force_z)