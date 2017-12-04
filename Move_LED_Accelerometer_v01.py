# Moves single LED based on input from the accelerometer x,y axes 

from microbit import *

x = 2
y = 2
display.set_pixel(x, y, 9)

def move_pixel(a,b):
    global x
    global y
    x = x + a
    y = y + b
    if x < 0:
        x = 0
    if x > 4:
        x = 4
    if y < 0:
        y = 0
    if y > 4:
        y = 4
    sleep(400)
    display.clear()
    display.set_pixel(x, y, 9)

while True:
    reading_x = accelerometer.get_x()
    if reading_x > 70:
        move_pixel(1,0)
    if reading_x < -70:
        move_pixel(-1,0)

    reading_y = accelerometer.get_y()
    if reading_y > 70:
        move_pixel(0,1)
    if reading_y < -70:
        move_pixel(0,-1)

        