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
MotorLf = Motor(Ports.PORT3, 6/1, False)
MotorLrt = Motor(Ports.PORT2, 6/1, False)
MotorLrb = Motor(Ports.PORT1,  6/1, False)
MotorRf = Motor(Ports.PORT4,  6/1, True)
MotorRrt = Motor(Ports.PORT6, 6/1, True)
MotorRrb = Motor(Ports.PORT5, 6/1, True)

#intake variables and motor
isForward = True
isOn = False
MotorI = Motor(Ports.PORT6, 6/1, True)

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
    '''while(controller.axis1.changed):
       axis1Pos = int(controller.axis1.position)
        velocity = axis1Pos
        #drive.drive(FORWARD, velocity**1.75)
        if(controller.axis2.changed):
            if(controller.axis1.position >= 0 && controller.axis2.position >= 0):
                velocity = math.sqrt((axis1Pos**2+controller.axis2.position**2)) * 1
            elif(controller.axis1.position <= 0 | controller.axis2.position <= 0):
                velocity = math.sqrt((axis1.position**2+axis2.position**2)) * -1
        drive.drive(FORWARD, velocity'''
    if(controller.axis1.changed):
        if(controller.axis1.position() > 0):
            right_group.spin(FORWARD,(controller.axis1.position() * 0.5) ** 2,PERCENT)
        elif(controller.axis1.position() == 0):
            right_group.stop
        else:
            right_group.spin(REVERSE, (controller.axis1.position() * 0.5)**2, PERCENT)
    
    if(controller.axis3.changed):
        if(controller.axis1.position() > 0):
            right_group.spin(FORWARD,(controller.axis3.position() * 0.5) ** 2,PERCENT)
        elif(controller.axis1.position() == 0):
            right_group.stop
        else:
            right_group.spin(REVERSE, (controller.axis3.position() * 0.5)**2, PERCENT)

    
def runIntake():
    if(isOn): # type: ignore
        isOn = False
        MotorI.stop()
    else:
        isOn = True
        if(isForward == True):#type:ignore
            if(controller.buttonR1.pressing == True):
                isForward = False
                MotorI.spin(REVERSE, 100, PERCENT)
            else:
                MotorI.spin(FORWARD, 100, PERCENT)
        else:
            if(controller.buttonR1.pressing == True):
                isForward = True
                MotorI.spin(FORWARD, 100, PERCENT)
            else:
                MotorI.spin(REVERSE, 100, PERCENT)



#MAKE SURE THIS IS AT THE END!!!!!!!
while True:
    printDetails()
    move()
    controller.buttonR2.pressed(runIntake)


        
