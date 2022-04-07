import socket
from time import sleep
import unicornhat
from pi.unicorn import bytes_to_matrix

# IP address and port of the receiving RPi
UDP_IP = "192.168.43.200"
UDP_PORT = 9000

# Set up UnicornHat
unicornhat.set_layout(unicornhat.AUTO)
unicornhat.rotation(0) # tested on pHAT/HAT with rotation 0, 90, 180 & 270
unicornhat.brightness(0.5)
u_width, u_height = unicornhat.get_shape()

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(192) # buffer size is 192 bytes

    # The data should be 3 * 64 = 192 bytes long
    # for i in range(u_width * u_height):
    #     r, g, b = data[i * 3], data[i * 3 + 1], data[i * 3 + 2]
    #     unicorn.set_pixel(i % 8, i // 8, r, g, b)
    mat = bytes_to_matrix(data, u_width, u_height)
    for x in range(u_width):
        for y in range(u_height):
            r, g, b = mat[y][x]
            unicornhat.set_pixel(x, y, r, g, b)
    unicornhat.show()
