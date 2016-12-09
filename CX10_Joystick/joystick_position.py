import pygame
import serial
import time
# Color RGB Tuples
black = (0, 0, 0)
white = ( 255, 255, 255)

# This is a simple class that will help us print to the screen
# It has nothing to do with the joysticks, just outputing the
# information.
class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def prints(self, screen, textString):
        textBitmap = self.font.render(textString, True, black)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10


pygame.init()
ser = serial.Serial('/dev/cu.usbmodem14111',115200)
# Set the width and height of the screen [width,height]
#size = [500, 700]
#screen = pygame.display.set_mode(size)

#pygame.display.set_caption("CX-10 Controller")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
#clock = pygame.time.Clock()

# Initialize the joysticks
#pygame.joystick.init()

# Get ready to print
#textPrint = TextPrint()

# Clear the drawing screen
#screen.fill(white)
#textPrint.reset()

# Get count of joysticks
#joystick_count = pygame.joystick.get_count()

# Joystick number to use, change this if you have more than one
joystick_number = 0

joystick = pygame.joystick.Joystick(joystick_number)
joystick.init()

# Get the name from the OS for the controller/joystick
name = joystick.get_name()
#textPrint.prints(screen, "Joystick name: {}".format(name) )

# Usually axis run in pairs, up/down for one, and left/right for
# the other.
axes = joystick.get_numaxes()
#textPrint.prints(screen, "Number of axes: {}".format(axes) )
#textPrint.indent()

#axes_2 = [{'Name':'Roll','AxNum':0},
#        {'Name':'Pitch','AxNum':1},
#        {'Name':'Yaw','AxNum':2},
#        {'Name':'Throttle','AxNum':3}]

# Main Loop
while done==False:

    # Process any user events
    for event in pygame.event.get():

        # Close program
        if event.type == pygame.QUIT:
            done=True

        # Joystick actions
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")




    for i in range( axes ):
        axis = joystick.get_axis( i )
        if i == 0:
            roll = round((axis*1000)/2)
        elif i == 1:
            pitch = round((axis*-1000)/2)
        elif i == 2:
            yaw = round((axis*1000)/2)
        elif i == 3:
            throttle = round((axis*-1000)/2)
        else:
            pass
    left_button = joystick.get_button(2)
    right_button = joystick.get_button(3)
    #    textPrint.prints(screen, "Axis {} value: {:>6.3f}".format(i, axis) )
    #textPrint.unindent()
    #print "%03d,%03d,%03d,%03d,%01d,%01d\n" %(throttle, pitch, roll, yaw, left_button, right_button)
    #ser.write("%03d,%03d,%03d,%03d\n" %(throttle, pitch, roll, yaw))
    ser.write("%03d,%03d,%03d,%03d,%01d,%01d\n" %(throttle, pitch, roll, yaw, left_button, right_button))
    ser.flush()

    # Go ahead and update the screen with what we've drawn.
    #pygame.display.flip()

    # Limit to 20 frames per second
    #clock.tick(10)
    #time.sleep(0.01)
# Close the window and quit.
pygame.quit()
