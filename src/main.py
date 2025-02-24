# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Chinm                                                        #
# 	Created:      11/6/2024, 8:19:56 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *
from movement import *
from intake import *

# Brain should be defined by default
brain=Brain()

#pneumatics
Pneumatic1 = DigitalOut(brain.three_wire_port.a)

#initialize the drivetrain and controller
drive = DriveTrain(left_group, right_group)
controller = Controller()

# Begin project code
def printDetails():
    brain.screen.clear_screen()
    brain.screen.set_cursor(1,1)

    brain.screen.print("Temperature:", drive.temperature(TemperatureUnits.FAHRENHEIT))
    brain.screen.next_row()

    # A brief delay to allow text to be printed without distortion or tearing
    wait(100,MSEC)

countOn = 0
countForward  = 0
isOn = False
global isForward


def pneumatic():
    if controller.buttonL1.pressing:
        Pneumatic1.set(True)
        brain.screen.print("pneumatic open")
    else:
        Pneumatic1.set(False)
        brain.screen.print("pneumatic close")

def driver_control():
    while True:
        drive()
        printDetails()
        pneumatic()
        #controller.buttonR2.pressed(runIntake())

def auton():
    printDetails()

#MAKE SURE THIS IS AT THE END!!!!!!!
def main():
    driver_control()
    competion = Competition(driver_control, auton)
    
main()



        
