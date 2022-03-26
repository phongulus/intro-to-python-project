from time import sleep
import controls

while True:
  
  if controls.is_up_pressed():
    print("up")

  if controls.is_down_pressed():
    print("down")

  if controls.is_left_pressed():
    print("left")

  if controls.is_right_pressed():
    print("right")

  if controls.is_center_pressed():
    print("center")

  if controls.is_A_pressed():
    print("A")

  if controls.is_B_pressed():
    print("B")

  sleep(0.5)
