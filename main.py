# include microbit
from microbit import *

# time representation
# import timer.py

# 25 minutes per pomodoro
pomodoroSlot = 25

global status


# press button once start the time countdown from 25 minutes
def startTimer(time):
    status = "running"
    display.scroll("Start")
    return status


# press button again pause the timer
def pauseTime():
    status = "paused"
    display.scroll("Pause")
    return status


# press button again will reset the time
def resetTimer(time):
    status = "reset"
    display.scroll("Reset")
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
