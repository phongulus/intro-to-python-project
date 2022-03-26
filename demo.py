from time import sleep
import controls
from send_unicorn import send_matrix_data

dot_coordinates = (3, 3)
x_max = 6
y_max = 6

def coor_to_mat(coor):
    mat = [0] * 8
    for y in range(8):
        row = []
        for x in range(8):
            if x in (coor[0], coor[0] + 1) and y in (coor[1], coor[1] + 1):
                row.append((255, 51, 153))
            else:
                row.append((0, 0, 0))
        mat[y] = row
    return mat

def update_coords(delta_x, delta_y):
    global dot_coordinates
    x, y = dot_coordinates
    if x + delta_x < 0 or x + delta_x > x_max or \
        y + delta_y < 0 or y + delta_y > y_max:
        pass
    else:
        dot_coordinates = (x, y)

while True:
  
    if controls.is_up_pressed():
        print("up")
        update_coords(0, 1)
        send_matrix_data(coor_to_mat(dot_coordinates))
        sleep(0.5)

    if controls.is_down_pressed():
        print("down")
        update_coords(0, -1)
        send_matrix_data(coor_to_mat(dot_coordinates))
        sleep(0.5)

    if controls.is_left_pressed():
        print("left")
        update_coords(-1, 0)
        send_matrix_data(coor_to_mat(dot_coordinates))
        sleep(0.5)

    if controls.is_right_pressed():
        print("right")
        update_coords(1, 0)
        send_matrix_data(coor_to_mat(dot_coordinates))
        sleep(0.5)

    if controls.is_center_pressed():
        print("center")
        sleep(0.5)

    if controls.is_A_pressed():
        print("A")
        sleep(0.5)

    if controls.is_B_pressed():
        print("B")
        sleep(0.5)