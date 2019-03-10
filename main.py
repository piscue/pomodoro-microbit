# include microbit
from microbit import *

# time representation
# import timer.py

# 25 minutes per pomodoro
pomodoroSlot = 25

global status

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

# press button once start the time countdown from 25 minutes
def startTimer(time):
    status = "running"
    display.scroll("3 2 1 GO")
    for i in range(0,time):
        time = time - 1
        display.show(imageNumber(time))
        sleep(500)
    display.show(Image.HAPPY)
    status = "paused"
    return status


# press button again pause the timer
def pauseTime():
    status = "paused"
    display.scroll("Pause")
    return status


# press button again will reset the time
def resetTimer(time):
    status = "reset"
    display.show(imageNumber(time))
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
