import pygame
import serial
import time


# Initialize pygame
pygame.init()

# This is the serial port for the Arduino. Be sure
# to change it for your particular setup.
ser = serial.Serial('/dev/cu.usbmodem1411',115200)

# Loop until the user clicks the close button.
done = False

# Joystick number to use, change this if you have more than one
joystick_number = 0

# Make a joystick object and initialize it
joystick = pygame.joystick.Joystick(joystick_number)
joystick.init()

# Usually axis run in pairs, up/down for one, and left/right for
# the other.
axes = joystick.get_numaxes()

# Main Loop
while done==False:

    # Process any user events
    for event in pygame.event.get():

        # Close program
        if event.type == pygame.QUIT:
            done=True

    # Get the values of the joystick and scale them. In
    # my setup the values range from -1 to 1. You can switch
    # the negtive signs if it is reversed on your equipment.
    # This will output a value of -500 to 500.
    for i in range(axes):
        axis = joystick.get_axis(i)
        if i == 0:
            roll = round(axis * 500)
        elif i == 1:
            pitch = round(axis * -500)
        elif i == 2:
            yaw = round(axis * 500)
        elif i == 3:
            throttle = round(axis * -500)
        else:
            pass

    # Get the state of the buttons we'll use to simulate the
    # left and right push buttons of the CX-10 remote.
    left_button = joystick.get_button(2)
    right_button = joystick.get_button(3)

    # Send it out the serial port!
    ser.write("%03d,%03d,%03d,%03d,%01d,%01d\n" %(throttle, pitch, roll, yaw, left_button, right_button))
    ser.flush()

# Close the window and quit.
pygame.quit()
