# fse103.py
#
# author: Wesley Liao
# email: wesliao@iu.edu
# 
# A class to interface with the Varience FSE103 force sensor (https://variense.com/product/fse103/)
#
# I am not affiliated with Varience in any way.
#

import serial
import struct

class FSE103():
    def __init__(self, port):
        self.serialport = serial.Serial(port, 9600)

        self.timestamp = 0
        self.mode = None

        self.force_x = 0.0
        self.force_y = 0.0
        self.force_z = 0.0

        self.raw_x = 0.0
        self.raw_y = 0.0
        self.raw_z = 0.0

    def read(self, timeout=10):
        # read( timeout=10)
        #
        # R
        readcount = 0

        while struct.unpack('B',self.serialport.read())[0] != 0x0d and readcount < timeout:
            readcount += 1

        if readcount < timeout:
            messagesize = struct.unpack('B',self.serialport.read())[0]
            messagetype = struct.unpack('B',self.serialport.read())[0]


            self.timestamp = struct.unpack('>I', self.serialport.read(4))[0]

            if messagetype == 0x66:
                self.mode = "force"
                self.force_x = struct.unpack('>f', self.serialport.read(4))[0]
                self.force_y = struct.unpack('>f', self.serialport.read(4))[0]
                self.force_z = struct.unpack('>f', self.serialport.read(4))[0]

            elif messagetype == 0x72:
                self.mode = "raw"
                self.raw_x = struct.unpack('>f', self.serialport.read(4))[0]
                self.raw_y = struct.unpack('>f', self.serialport.read(4))[0]
                self.raw_z = struct.unpack('>f', self.serialport.read(4))[0]

    def set_raw_values(self):
        self.serialport.write(b'r')

    def set_forces(self):
        self.serialport.write(b'f')

    def initialize_sensor(self):
        self.serialport.write(b'z')





