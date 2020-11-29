import sys
import RPi.GPIO as GPIO
import time
import evdev
import logging

from builtins import range

logging.basicConfig(filename='/var/log/rat.log', filemode='w', format='%(asctime)s - %(message)s')

GPIO.setmode(GPIO.BOARD)
armPin = 19
directionPin = 11
stepPin = 12
GPIO.setup(armPin, GPIO.IN)
GPIO.setup(armPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(directionPin, GPIO.OUT)
GPIO.setup(stepPin, GPIO.OUT)

GPIO.output(directionPin, GPIO.LOW)


def move(direction, steps):
    if direction == "pull":
        GPIO.output(directionPin, GPIO.HIGH)
    else:
        GPIO.output(directionPin, GPIO.LOW)

    GPIO.output(stepPin, GPIO.LOW)
    for _ in range(0, steps):
        GPIO.output(stepPin, GPIO.HIGH)
        time.sleep(0.01)
        GPIO.output(stepPin, GPIO.LOW)


try:
    while True:
        DEVICE = None
        DEVICES = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
        for d in DEVICES:
            if 'PixArt USB Optical Mouse' in d.name:
                DEVICE = d
                logging.info('Found (computer) mouse %s at %s...' % (d.name, d.path))
                break

        if DEVICE is None:
            sys.exit('could not find mouse')

        while GPIO.input(armPin) == 1:
            time.sleep(0.01)

        # allow the hunter to place the flap into position
        logging.info("trap is armed")
        move("pull", 80)
        time.sleep(10)
        move("push", 50)

        for event in DEVICE.read_loop():
            DEVICE.close()
            logging.info("CATCH IT")
            move("pull", 50)
            move("push", 80)
            break
finally:
    GPIO.cleanup(directionPin)
    GPIO.cleanup(stepPin)
    GPIO.cleanup(armPin)
