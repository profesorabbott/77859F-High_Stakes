from vex import *
from movement import *

brain = Brain()
MotorI = Motor(Ports.PORT7, 18/1, True)
intakeCount = -1

directionCount
intakeSpeed = 150

def toggleIntake():
    print(intakeCount)
    intakeCount *= -1

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