# include microbit
from microbit import *
from image import imageNumber

# time representation
# import timer.py

# 25 minutes per pomodoro
pomodoroSlot = 25

global status, seconds


# press button once start the time countdown from 25 minutes
def startTimer(time):
    status = "running"
    display.scroll("3 2 1 GO")
    # for i in range(0, time):
    #     time = time - 1
    #     display.show(imageNumber(time))
    #     sleep(500)
    # display.show(Image.HAPPY)
    # status = "paused"
    return status, time


# press button again pause the timer
def pauseTime():
    status = "paused"
    actualTime = ""
    return status, actualTime


# press button again will reset the time
def resetTimer(time):
    status = "reset"
    display.show(imageNumber(time))
    actualTime = time
    return status, actualTime


status = resetTimer(pomodoroSlot)
seconds = 60
# create a loop that don't block button input and allows to update the timer
while True:
    if button_a.is_pressed():
        print("button a pressed")
        if status[0] == "running":
            status = pauseTime()
        if status[0] == "paused":
            status = resetTimer(pomodoroSlot)
        if status[0] == "reset":
            print("status reset")
            status = startTimer(pomodoroSlot)
            actualTime = status[1]
    # print(status)
    if status[0] == "running":
        if actualTime <= pomodoroSlot and actualTime > -1:
            seconds = seconds + 1
            print(seconds)
            if seconds == 60:
                actualTime = actualTime - 1
                seconds = 0
            print(actualTime)
            # if image contains 7 replace by 9 else replace by 7
            printTime = imageNumber(actualTime)
            display.show(printTime)
            sleep(1000)
        else:
            print(actualTime)
            display.show(Image.HAPPY)
            status = "paused"
