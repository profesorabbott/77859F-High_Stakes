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

# Brain should be defined by default
brain=Brain()

MotorI = Motor(Ports.PORT7, 18/1, True)
intakeCount = -1

countOn = 0
countForward  = 0
isOn = False
global isForward

MotorLf = Motor(Ports.PORT3, 6/1, True)
MotorLrt = Motor(Ports.PORT2, 6/1, False)
MotorLrb = Motor(Ports.PORT1,  6/1, True)
MotorRf = Motor(Ports.PORT4,  6/1, False)
MotorRrt = Motor(Ports.PORT6, 6/1, True)
MotorRrb = Motor(Ports.PORT5, 6/1, False)

directionCount = -1
direction =FORWARD
intakeSpeed = 150

left_group = MotorGroup(MotorLf, MotorLrb, MotorLrt)
right_group = MotorGroup(MotorRf, MotorRrb, MotorRrt)
#pneumatics
Pneumatic1 = DigitalOut(brain.three_wire_port.a)

#initialize the drivetrain and controller
drivetrain = DriveTrain(left_group, right_group)
controller = Controller()

# Begin project code
def printDetails():
    brain.screen.clear_screen()
    brain.screen.set_cursor(1,1)

    brain.screen.print("Temperature:", drive.temperature(TemperatureUnits.FAHRENHEIT))
    brain.screen.next_row()

    # A brief delay to allow text to be printed without distortion or tearing
    wait(100,MSEC)



def drive():
    MotorLf.set_velocity(((controller.axis3.position()/100)**3)*100, PERCENT)
    MotorLrt.set_velocity(((controller.axis3.position()/100)**3)*100, PERCENT)
    MotorLrb.set_velocity(((controller.axis3.position()/100)**3)*100, PERCENT)
    
    MotorRf.set_velocity(((controller.axis2.position()/100)**3)*100, PERCENT)
    MotorRrt.set_velocity(((controller.axis2.position()/100)**3)*100, PERCENT)
    MotorRrb.set_velocity(((controller.axis2.position()/100)**3)*100, PERCENT)
    
    right_group.spin(FORWARD)
    left_group.spin(FORWARD)
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
        runIntake()

def auton():
    printDetails()

def toggleIntake(y):
    if y:
        intakeCount = 1
    else:
        intakeCount = -1

def reverseIntakeDir():
    global directionCount 
    global direction
    directionCount *= -1 
    print(directionCount)
    print(direction) # type: ignore
    if directionCount > 0:
        direction = REVERSE
        intakeSpeed = 75
    else:
        direction = FORWARD
        intakeSpeed = 150

def runIntake():
    if controller.buttonR2.pressing:
        toggleIntake(True)
        if controller.buttonR1.pressed:
            reverseIntakeDir()
    else:
        toggleIntake(False)
    if intakeCount > 0:
        MotorI.spin(direction, intakeSpeed, RPM)
    else:
        MotorI.stop()
    

#MAKE SURE THIS IS AT THE END!!!!!!!
def main():
    driver_control()
    competion = Competition(driver_control, auton)
    
main()



        
