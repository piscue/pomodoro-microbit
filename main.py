# include microbit
from microbit import *

# time representation
# import timer.py

# 25 minutes per pomodoro
pomodoroSlot = 25

global status

def ten():
    imageNumber = Image("70777:"
                        "70707:"
                        "70707:"
                        "70707:"
                        "70777")
    return imageNumber


def twenty():
    imageNumber = Image("77777:"
                        "07707:"
                        "77707:"
                        "70707:"
                        "77777")
    return imageNumber


def imageNumber(number):
    switch (number){
        case 25:
            imageNumber = Image("77777:"
                                "07700:"
                                "77777:"
                                "70707:"
                                "77777")

    24 = Image("77707:"
               "07707:"
               "77777:"
               "70007:"
               "77007")

    23 = Image("77777:"
               "07007:"
               "77777:"
               "70007:"
               "77777")
    }
# press button once start the time countdown from 25 minutes
def startTimer(time):
    status = "running"
    display.scroll("Start")
    image = twenty()
    display.show(image)
    return status


# press button again pause the timer
def pauseTime():
    status = "paused"
    display.scroll("Pause")
    return status


# press button again will reset the time
def resetTimer(time):
    status = "reset"
    imageNumber(time)
    return status


status = resetTimer(pomodoroSlot)

while True:
    if button_a.is_pressed():
        if status == "running":
            status = pauseTime()
        if status == "paused":
            status = resetTimer(pomodoroSlot)
        if status == "reset":
            status = startTimer(pomodoroSlot)
