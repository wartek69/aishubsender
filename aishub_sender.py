import logging
import serial
import socket
import argparse
logging.basicConfig(level=logging.INFO,
            format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s')


#Either a com port for windows or /dev/tty* port for unix
serial_port = '/dev/ttyACM0'
baudrate = 38400

#Change this for your usecase
aishub_address = ('aishub', 1111)

if __name__ == '__main__':
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    logging.info('Starting up serial ais reader...')
    with serial.Serial(serial_port, baudrate, timeout = 5) as ser:
        while True:
            aisdata = ser.readline()
            logging.info(aisdata)
            UDPClientSocket.sendto(aisdata, aishub_address)


