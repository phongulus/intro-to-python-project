import socket

# IP address and port of the receiving RPi
UDP_IP = "192.168.43.200"
UDP_PORT = 9000

# print("UDP target IP: %s" % UDP_IP)
# print("UDP target port: %s" % UDP_PORT)
# print("message: %s" % MESSAGE)
 
# sock = socket.socket(socket.AF_INET, # Internet
#                      socket.SOCK_DGRAM) # UDP
# sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

def send_matrix_data(mat):
    """
    Send the LED matrix color data to the remote UnicornHat.
    Takes `mat` as an argument, which is a 2D list of tuples
    `(r, g, b)`.
    """
    to_send = b''
    for y in mat:
        for x in y:
            to_send += x[0].to_bytes(1, 'little')
            to_send += x[1].to_bytes(1, 'little')
            to_send += x[2].to_bytes(1, 'little')
    sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    sock.sendto(to_send, (UDP_IP, UDP_PORT))
    sock.sendto(to_send, (UDP_IP, UDP_PORT))