import socket

# IP address and port of the receiving RPi
UDP_IP = "192.168.43.200"
UDP_PORT = 9000

def matrix_to_bytes(mat: list[list[tuple[int, int, int]]]) -> bytes:
    """
    Convert an (r, g, b) matrix to a sequence of bytes that can be
    sent via UDP to the Raspberry Pi with the LED matrix.

    Parameters:
    ----
    `mat <list[list[tuple[int, int, int]]]>`: The rows * columns matrix
    where each element is a tuple representing the color of a pixel via
    RGB code in a tuple `(r, g, b)`.

    Return:
    ----
    `data <bytes>`: The sequence of bytes, of length rows * columns.
    """

    data = b''
    for y in mat:
        for x in y:
            data += x[0].to_bytes(1, 'little')
            data += x[1].to_bytes(1, 'little')
            data += x[2].to_bytes(1, 'little')
    return data


def send_matrix_data(mat: list[list[tuple[int, int, int]]]) -> None:
    """
    Send the LED matrix color data to the remote UnicornHat.
    Takes `mat` as an argument, which is a 2D list of tuples
    `(r, g, b)`.

    Parameters:
    ----
    `mat <list[list[tuple[int, int, int]]]>`: The rows * columns matrix
    where each element is a tuple representing the color of a pixel via
    RGB code in a tuple `(r, g, b)`.

    Return:
    ----
    None
    """

    to_send = matrix_to_bytes(mat)
    sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP

    # Send matrix data three times to make sure that the LED matrix
    # Raspberry Pi receives it.
    sock.sendto(to_send, (UDP_IP, UDP_PORT))
    sock.sendto(to_send, (UDP_IP, UDP_PORT))
    sock.sendto(to_send, (UDP_IP, UDP_PORT))

    return None