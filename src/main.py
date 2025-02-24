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

#organize the motors into motor groups
#left_group = MotorGroup(MotorLf, MotorLrb, MotorLrt)
#right_group = MotorGroup(MotorRf, MotorRrb, MotorRrt)

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


def intake():
    brain.screen.clear_screen()
    brain.screen.set_cursor(1,1)
    brain.screen.print("entering the R1 loop")
    brain.screen.next_row()
    if controller.buttonR1.pressing:
        brain.screen.print("in the R1 loop")
        brain.screen.next_row()
        #toggleIntakeDir()
        brain.screen.print("direction toggled")
        brain.screen.next_row()
        wait(0.5, SECONDS)
        
    brain.screen.print("entering the R2 loop")
    brain.screen.next_row()
    #if controller.buttonR2.pressed:
    print('i am in R2')
    brain.screen.print("in the R2 loop")
    brain.screen.next_row()
    #toggleIntake()
    brain.screen.print("intake toggled")
    brain.screen.next_row()
    wait(0.2, MSEC)
    """ if intakeCount > 0:
        print('i am in intake count >0')
        brain.screen.print("intake on")
        brain.screen.next_row()
        #MotorI.spin(direction, intakeSpeed, RPM)
    else:
        brain.screen.print("intake off")
        brain.screen.next_row()
        #MotorI.stop()
    """
def pneumatic():
    if controller.buttonL1.pressing:
        Pneumatic1.set(True)
        brain.screen.print("pneumatic open")
    else:
        Pneumatic1.set(False)
        brain.screen.print("pneumatic close")

def driver_control():
    while True:
        move()
        printDetails()
        pneumatic()
    #controller.buttonR2.pressed(intake)

def auton():
    printDetails()

#MAKE SURE THIS IS AT THE END!!!!!!!
def main():
    driver_control()
    competion = Competition(driver_control, auton)
    
main()



        
