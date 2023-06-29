#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
# GPIO SETUP
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)


def callback(channel: int) -> None:
    """Function to print message when sound detected (input pin changes)."""
    if GPIO.input(channel):
        logging.info("Sound detected!")
    else:
        logging.info("Sound detected!")


GPIO.add_event_detect(
    channel, GPIO.BOTH, bouncetime=300
)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(
    channel, callback
)  # assign function to GPIO PIN, Run function on change

# infinite loop
while True:
    # print(GPIO.input(channel))
    time.sleep(0.1)
