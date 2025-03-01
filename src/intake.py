def toggleIntake():
    global intakeCount
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

def runIntake():
    if controller.buttonR1.pressing:
        reverseIntakeDir()
        wait(1.5, SECONDS)
        
    brain.screen.print("entering the R2 loop")
    brain.screen.next_row()
    if controller.buttonR2.pressed:
        print('i am in R2')
        brain.screen.print("in the R2 loop")
        brain.screen.next_row()
        toggleIntake()
        brain.screen.print("intake toggled")
        brain.screen.next_row()
        wait(0.2, MSEC)
    if intakeCount > 0:
        print('i am in intake count >0')
        brain.screen.print("intake on")
        brain.screen.next_row()
        MotorI.spin(direction, intakeSpeed, RPM)
    else:
        brain.screen.print("intake off")
        brain.screen.next_row()
        MotorI.stop()
    