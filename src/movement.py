from vex import *

brain  = Brain()

MotorLf = Motor(Ports.PORT3, 6/1, True)
MotorLrt = Motor(Ports.PORT2, 6/1, False)
MotorLrb = Motor(Ports.PORT1,  6/1, True)
MotorRf = Motor(Ports.PORT4,  6/1, False)
MotorRrt = Motor(Ports.PORT6, 6/1, True)
MotorRrb = Motor(Ports.PORT5, 6/1, False)

directionCount = -1
direction =FORWARD

left_group = MotorGroup(MotorLf, MotorLrb, MotorLrt)
right_group = MotorGroup(MotorRf, MotorRrb, MotorRrt)

#def drive():
