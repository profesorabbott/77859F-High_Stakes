from vex import *
from main import *
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

def drive():
    MotorLf.set_velocity(((controller.axis3.position()/100)**3)*100, PERCENT)
    MotorLrt.set_velocity(((controller.axis3.position()/100)**3)*100, PERCENT)
    MotorLrb.set_velocity(((controller.axis3.position()/100)**3)*100, PERCENT)
    
    MotorRf.set_velocity(((controller.axis2.position()/100)**3)*100, PERCENT)
    MotorRrt.set_velocity(((controller.axis2.position()/100)**3)*100, PERCENT)
    MotorRrb.set_velocity(((controller.axis2.position()/100)**3)*100, PERCENT)
    
    right_group.spin(FORWARD)
    left_group.spin(FORWARD)