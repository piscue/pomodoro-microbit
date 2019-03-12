# include microbit
from microbit import *

def imageNumber(number):
    return {
        25: Image("77777:"
                  "07700:"
                  "77777:"
                  "70007:"
                  "77777"),
        24: Image("77707:"
                  "07707:"
                  "77777:"
                  "70007:"
                  "77007"),
        23: Image("77777:"
                  "07007:"
                  "77777:"
                  "70007:"
                  "77777"),
        22: Image("77777:"
                  "07007:"
                  "77777:"
                  "70700:"
                  "77777"),
        21: Image("77007:"
                  "07077:"
                  "77007:"
                  "70007:"
                  "77007"),
        20: Image("77777:"
                  "07707:"
                  "77707:"
                  "70707:"
                  "77777"),
        19: Image("07777:"
                  "77707:"
                  "07777:"
                  "07007:"
                  "07007"),
        18: Image("07777:"
                  "77707:"
                  "07777:"
                  "07707:"
                  "07777"),
        17: Image("07777:"
                  "77007:"
                  "07007:"
                  "07070:"
                  "07700"),
        16: Image("07777:"
                  "77700:"
                  "07777:"
                  "07707:"
                  "07777"),
        15: Image("07777:"
                  "77700:"
                  "07777:"
                  "07007:"
                  "07777"),
        14: Image("07707:"
                  "77707:"
                  "07777:"
                  "07007:"
                  "07007"),
        13: Image("07777:"
                  "77007:"
                  "07777:"
                  "07007:"
                  "07777"),
        12: Image("07777:"
                  "77007:"
                  "07777:"
                  "07700:"
                  "07777"),
        11: Image("07007:"
                  "77077:"
                  "07007:"
                  "07007:"
                  "07007"),
        10: Image("07777:"
                  "77707:"
                  "07707:"
                  "07707:"
                  "07777"),
        9: Image("00777:"
                 "00707:"
                 "00777:"
                 "00007:"
                 "00007"),
        8: Image("00777:"
                 "00707:"
                 "00777:"
                 "00707:"
                 "00777"),
        7: Image("00777:"
                 "00007:"
                 "00007:"
                 "00070:"
                 "00700"),
        6: Image("00777:"
                 "00700:"
                 "00777:"
                 "00707:"
                 "00777"),
        5: Image("00777:"
                 "00700:"
                 "00777:"
                 "00007:"
                 "00777"),
        4: Image("00707:"
                 "00707:"
                 "00777:"
                 "00007:"
                 "00007"),
        3: Image("00777:"
                 "00007:"
                 "00777:"
                 "00007:"
                 "00777"),
        2: Image("00777:"
                 "00007:"
                 "00777:"
                 "00700:"
                 "00777"),
        1: Image("00007:"
                 "00077:"
                 "00007:"
                 "00007:"
                 "00007"),
        0: Image("00777:"
                 "00707:"
                 "00707:"
                 "00707:"
                 "00777")
    }.get(number, "90009"
                  "09090"
                  "00900"
                  "09090"
                  "90009")


# 25 minutes per pomodoro
pomodoroSlot = 25

global status, seconds


# press button once start the time countdown from 25 minutes
def startTimer(time):
    status = "running"
    display.scroll("focus")
    return status, time


# press button again pause the timer
def pauseTime():
    status = "paused"
    actualTime = pomodoroSlot
    return status, actualTime


# press button again will reset the time
def resetTimer(time):
    status = "reset"
    display.show(imageNumber(time))
    actualTime = time
    return status, actualTime


def flashing():
    for x in range(0, 5):
        for y in range(0, 5):
            if display.get_pixel(x, y) == 7:
                display.set_pixel(x, y, 9)
            else:
                if display.get_pixel(x, y) == 9:
                    display.set_pixel(x, y, 7)


status = resetTimer(pomodoroSlot)
seconds = 60

# create a loop that don't block button input and allows to update the timer
while True:
    if button_a.is_pressed():
        if status[0] == "running":
            status = pauseTime()
            sleep(2000)
            display.show(printTime)
        else:
            if status[0] == "paused":
                display.scroll("x")
                status = resetTimer(pomodoroSlot)
                seconds = 60
            else:
                if status[0] == "reset":
                    status = startTimer(pomodoroSlot)
                    actualTime = status[1]
    if status[0] == "running":
        if actualTime <= pomodoroSlot and actualTime > -1:
            if seconds == 60:
                actualTime = actualTime - 1
                seconds = 0
                printTime = imageNumber(actualTime)
                display.show(printTime)
            seconds = seconds + 1
            flashing()
            sleep(1000)
        else:
            display.show(Image.HAPPY)
            status = "paused", pomodoroSlot