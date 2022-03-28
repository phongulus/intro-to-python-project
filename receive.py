import socket
from time import sleep
import unicornhat as unicorn

# IP address and port of the receiving RPi
UDP_IP = "192.168.43.200"
UDP_PORT = 9000

# Set up UnicornHat
unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0) # tested on pHAT/HAT with rotation 0, 90, 180 & 270
unicorn.brightness(0.5)
u_width, u_height=unicorn.get_shape()

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(192) # buffer size is 1024 bytes

    # The data should be 3 * 64 = 192 bytes long
    for i in range(u_width * u_height):
        r, g, b = data[i * 3], data[i * 3 + 1], data[i * 3 + 2]
        unicorn.set_pixel(i % 8, i // 8, r, g, b)
    unicorn.show()
    # print("Updated UnicornHat!")
    # sleep(0.2)