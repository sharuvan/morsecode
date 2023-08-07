from microbit import *
from static import MORSECODE, DOT, DASH, CLOCK

# set constants
SYNC_THRESHOLD = 150
DOT_THRESHOLD = 250
DASH_THRESHOLD = 500

# initialize variables
buffer = ''
time_start = running_time()
epoch = 0

# receiver shows R
display.show('R')
# cancel pin2 initial activation
pin2.read_digital()

def activation_duration_swapped():
    # calculate delta: time elapsed since epoch
    delta = round(running_time() / 1000) - epoch
    # swap activation duration every minute
    if int((delta / 60) % 2) == 0: return False
    else: return True

def get_dot_threshold():
    # fetch alternating dot threshold
    if activation_duration_swapped(): return DASH_THRESHOLD
    else: return DOT_THRESHOLD

def get_dash_threshold():
    # fetch alternating dash threshold
    if activation_duration_swapped(): return DOT_THRESHOLD
    else: return DASH_THRESHOLD

def detect_dot():
    # actions when dot detected
    global buffer
    buffer += '.'
    display.show(Image(DOT))

def detect_dash():
    # actions when dash detected
    global buffer
    buffer += '-'
    display.show(Image(DASH))

while True:
    waiting = running_time() - time_start
    time_on = None
    # read and record signal-in time
    while pin2.read_digital():
        if not time_on:
            time_on = running_time()

    time_off = running_time()
    if time_on:
        # when signal is cut off, save in buffer and display code
        time_start = running_time()
        duration = time_off - time_on
        if duration < SYNC_THRESHOLD:
            epoch = round(running_time() / 1000)
            display.show(Image(CLOCK))
        elif duration < DOT_THRESHOLD:
            if activation_duration_swapped(): detect_dash()
            else: detect_dot()
        elif duration < DASH_THRESHOLD:
            if activation_duration_swapped(): detect_dot()
            else: detect_dash()
            
    elif (len(buffer) > 0 and waiting > DASH_THRESHOLD) or len(buffer) == 5:
        # if buffer have data and waiting time exceeds dash threshold
        # decode character, reset buffer and display
        character = MORSECODE.get(buffer, '?')
        buffer = ''
        display.show(character)
      