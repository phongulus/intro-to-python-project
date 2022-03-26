from time import sleep
import controls

while True:
  
  if controls.is_up_pressed():
    print("up")
    sleep(0.2)

  if controls.is_down_pressed():
    print("down")
    sleep(0.2)

  if controls.is_left_pressed():
    print("left")
    sleep(0.2)

  if controls.is_right_pressed():
    print("right")
    sleep(0.2)

  if controls.is_center_pressed():
    print("center")
    sleep(0.2)

  if controls.is_A_pressed():
    print("A")
    sleep(0.2)

  if controls.is_B_pressed():
    print("B")
    sleep(0.2)