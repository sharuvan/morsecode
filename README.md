# IoT Worksheet 2 documentation

## Ahmed Sharuvan [22023493]

A morse code transmitter and receiver is implemented to run on the BBC Microbit using its MicroPython API.

The transmitter and receiver uses the international morse code sequences to send messages over through the GPIO cable. An encyphering mechanism is used to make it harder for an adversary to tap into and figure out the messages sent over the wires. This is achieved by using a activation swapping function shared between the devices which swaps the activation duration for each of the signals used. The swapping is done every minute and the devices synchronize and acknowledge an epoch time by using a dedicated signal making the communication very much difficult to figure out by an intermediary.

## How it works
- Flash the two devices with the respective python scripts for transmitter and receiver.
- Connect GPIO pin 2 on each devices together.
- The transmitter presses button A and B at the same time to send the time synchronization signal for use with enciphering. A clock should appear on both devices when this is done.
- Press button A to transmit a Dot and button B to transmit a dash consecutively until the character is fully expressed.
- When completed, wait for a second and the decoded character should appear on the receiver.