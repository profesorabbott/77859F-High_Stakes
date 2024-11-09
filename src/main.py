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

#instantiate the left and right motors; f is front, rb is rear bottom, rt is rear top
MotorLf = Motor(Ports.PORT3, 6/1, True)
MotorLrt = Motor(Ports.PORT2, 6/1, False)
MotorLrb = Motor(Ports.PORT1,  6/1, True)
MotorRf = Motor(Ports.PORT4,  6/1, False)
MotorRrt = Motor(Ports.PORT6, 6/1, True)
MotorRrb = Motor(Ports.PORT5, 6/1, False)

#intake motor
MotorI = Motor(Ports.PORT7, 18/1, True)

#pneumatics
Pneumatic1 = DigitalOut(brain.three_wire_port.a)

#organize the motors into motor groups
left_group = MotorGroup(MotorLf, MotorLrb, MotorLrt)
right_group = MotorGroup(MotorRf, MotorRrb, MotorRrt)

#initialize the drivetrain and controller
drive = DriveTrain(left_group, right_group)
controller = Controller()

    

# Begin project code
def printDetails():
    brain.screen.clear_screen()
    brain.screen.set_cursor(1,1)

    brain.screen.print("Velocity:", drive.velocity(PERCENT))
    brain.screen.next_row()

    brain.screen.print("Current:", drive.current(CurrentUnits.AMP))
    brain.screen.next_row()

    brain.screen.print("Power:", drive.power(PowerUnits.WATT))
    brain.screen.next_row()

    brain.screen.print("Torque:", drive.torque(TorqueUnits.NM))
    brain.screen.next_row()

    brain.screen.print("Efficiency:", drive.efficiency(PERCENT))
    brain.screen.next_row()

    brain.screen.print("Temperature:", drive.temperature(TemperatureUnits.FAHRENHEIT))
    brain.screen.next_row()

    # A brief delay to allow text to be printed without distortion or tearing
    wait(100,MSEC)

def move():
    MotorLf.set_velocity(((controller.axis3.position()/100)**3)*100, PERCENT)
    MotorLrt.set_velocity(((controller.axis3.position()/100)**3)*100, PERCENT)
    MotorLrb.set_velocity(((controller.axis3.position()/100)**3)*100, PERCENT)
    
    MotorRf.set_velocity(((controller.axis2.position()/100)**3)*100, PERCENT)
    MotorRrt.set_velocity(((controller.axis2.position()/100)**3)*100, PERCENT)
    MotorRrb.set_velocity(((controller.axis2.position()/100)**3)*100, PERCENT)
    
    right_group.spin(FORWARD)
    left_group.spin(FORWARD)

countOn = 0
countForward  = 0
isOn = False
global isForward

'''def forwardCount():

    countForward += 1


def setIntakeDir():
    if countForward % 2 == 0:
         return False
    else:
        return True
    forwardCount()
'''

'''
def intake():
    if countOn % 2 == 0:
        isOn = True
        
    else:
        isOn = False
    
    if(controller.buttonR1.pressing):
        isForward = True
    elif(controller.buttonL1.pressing):
        isForward = False
    
    if isOn:
        if isForward:
            if controller.buttonR1.pressing:
                isForward = False
                MotorI.spin(REVERSE, 100, PERCENT)
            else:
                MotorI.spin(FORWARD, 100, PERCENT)
        else:
            if controller.buttonR1.pressing:
                isForward = True
                MotorI.spin(FORWARD, 100, PERCENT)
            else:
                MotorI.spin(REVERSE, 100, PERCENT)
    else:
        MotorI.stop()
    

def runIntake():
    controller.buttonR2.pressed(intake)
'''
global directionCount
global direction
intakeCount = -1
directionCount = -1
direction = FORWARD
intakeSpeed = 150

def toggleIntake():
    global intakeCount
    print(intakeCount)
    intakeCount *= -1


def toggleIntakeDir():
    directionCount *= -1 # type: ignore
    print(directionCount)
    print(direction) # type: ignore
    if directionCount > 0:
        direction = FORWARD
        intakeSpeed = 150
    else:
        direction = REVERSE
        intakeSpeed = 75


def intake():
    brain.screen.clear_screen()
    brain.screen.set_cursor(1,1)
    brain.screen.print("entering the R1 loop")
    brain.screen.next_row()
    if controller.buttonR1.pressing:
        brain.screen.print("in the R1 loop")
        brain.screen.next_row()
        toggleIntakeDir()
        brain.screen.print("direction toggled")
        brain.screen.next_row()
        wait(0.5, SECONDS)
        
    brain.screen.print("entering the R2 loop")
    brain.screen.next_row()
    if controller.buttonR2.pressing:
        brain.screen.print("in the R2 loop")
        brain.screen.next_row()
        toggleIntake()
        brain.screen.print("intake toggled")
        brain.screen.next_row()
        wait(0.2, MSEC)
        if intakeCount > 0:
            brain.screen.print("intake on")
            brain.screen.next_row()
            MotorI.spin(direction, intakeSpeed, RPM)
        else:
            brain.screen.print("intake off")
            brain.screen.next_row()
            MotorI.stop()
        

def driver_control():
    while True:
        #move()
        printDetails()
        intake()

def auton():
    printDetails()

#MAKE SURE THIS IS AT THE END!!!!!!!
def main():
    driver_control()
    competion = Competition(driver_control, auton)
    
main()



        
