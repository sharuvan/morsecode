from microbit import *
import music
from static import DOT, DASH, CLOCK

# set constants
SYNC_DURATION = 105
DOT_DURATION = 205
DASH_DURATION = 450

#initialize variables
epoch = 0

# transmitter shows T
display.show('T')

def activation_duration_swapped():
    # calculate delta: time elapsed since epoch
    delta = round(running_time() / 1000) - epoch
    # swap activation duration every minute
    if int((delta / 60) % 2) == 0: return False
    else: return True

def get_dot_duration():
    # fetch alternating dot duration
    if activation_duration_swapped(): return DASH_DURATION
    else: return DOT_DURATION

def get_dash_duration():
    # fetch alternating dash duration
    if activation_duration_swapped(): return DOT_DURATION
    else: return DASH_DURATION

while True:
    # test button presses in a loop
    if button_a.is_pressed() and button_b.is_pressed():
        # synchronize epoch time when button a and b is pressed
        # at the same time
        pin2.write_digital(1)
        music.pitch(800, duration=SYNC_DURATION, wait=True)
        pin2.write_digital(0)
        sleep(50)
        epoch = round(running_time() / 1000)
        display.show(Image(CLOCK))
    elif button_a.is_pressed():
        # transmit dot signal when button a is pressed
        display.show(Image(DOT))
        pin2.write_digital(1)
        music.pitch(800, duration=get_dot_duration(), wait=True)
        pin2.write_digital(0)
        sleep(50)
        display.clear()
    elif button_b.is_pressed():
        # transmit dash signal when button a is pressed
        display.show(Image(DASH))
        pin2.write_digital(1)
        music.pitch(800, duration=get_dash_duration(), wait=True)
        pin2.write_digital(0)
        sleep(50)
        display.clear()
