"""
Program referenced from :
https://bitbucket.org/MattHawkinsUK/rpispy-misc/raw/master/python/stepper.py

Attention : Original program is python 2.x

I add a coefficient for transform running time to distance (accuracy not high)

Motor power controled by a relay module,
power will be reset when start running, and switch after initialization.
"""


import time
import RPi.GPIO as GPIO
import relay_lib_seeed as relay


length = 5     # mm
coe = 0.23  # 10 mm per 40 second (0.25mm/1s)

# Reset motor power
relay_port = 2
relay.relay_off(relay_port)

# Use BCM GPIO references instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO signals to use
# Physical pins 11,15,16,18
# GPIO17,GPIO22,GPIO23,GPIO24
StepPins = [17, 22, 23, 24]

# Set all pins as output
for pin in StepPins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

# Define advanced sequence as shown in manufacturers datasheet
Seq = [[1, 0, 0, 1],
       [1, 0, 0, 0],
       [1, 1, 0, 0],
       [0, 1, 0, 0],
       [0, 1, 1, 0],
       [0, 0, 1, 0],
       [0, 0, 1, 1],
       [0, 0, 0, 1]]

StepCount = len(Seq)
StepDir = 1  # Set to 1 or 2 for clockwise
# Set to -1 or -2 for anti-clockwise

# Initialise variables
StepCounter = 0

# Start main loop
if __name__ == "__main__":
    try:
        relay.relay_on(relay_port)
        print('Motor power on')

        timeticnow = 0

        while True:
            for pin in range(0, 4):
                xpin = StepPins[pin]
                if Seq[StepCounter][pin] != 0:
                    GPIO.output(xpin, True)
                else:
                    GPIO.output(xpin, False)

            StepCounter += StepDir

            # If we reach the end of the sequence
            # start again
            if StepCounter >= StepCount:
                StepCounter = 0
            if StepCounter < 0:
                StepCounter = StepCount + StepDir

            # Wait before moving on
            time.sleep(0.0009)

            timeticnow = timeticnow + 0.0009
            posnow = timeticnow * coe

            if posnow >= length:
                break

        # Stop signal and cut power of motor
        for pin in StepPins:
            GPIO.output(pin, False)

        relay.relay_off(relay_port)
        print('Motor stop, power off')

    except KeyboardInterrupt:
        for pin in StepPins:
            GPIO.output(pin, False)
        relay.relay_off(relay_port)

        print('Motor stop by keyboard input, power off')
