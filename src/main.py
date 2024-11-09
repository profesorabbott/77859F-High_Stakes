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
MotorI = Motor(Ports.PORT7, 6/1, True)

#pneumatics
Pneumatic1 = DigitalOut(brain.three_wire_port.a)
Pneumatic2 = DigitalOut(brain.three_wire_port.b)

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
    MotorLf.set_velocity(controller.axis3.position(), PERCENT)
    MotorLrt.set_velocity(controller.axis3.position(), PERCENT)
    MotorLrb.set_velocity(controller.axis3.position(), PERCENT)
    
    MotorRf.set_velocity(controller.axis2.position(), PERCENT)
    MotorRrt.set_velocity(controller.axis2.position(), PERCENT)
    MotorRrb.set_velocity(controller.axis2.position(), PERCENT)
    
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


def runIntake():
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




#MAKE SURE THIS IS AT THE END!!!!!!!
while True:
    printDetails()
    move()
    controller.buttonR2.pressed(runIntake)
    countForward+=1
    



        
