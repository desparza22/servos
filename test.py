from gpiozero import Servo
from time import sleep

servo = Servo(25, min_pulse_width=(.5/1000.), max_pulse_width=(2.5/1000.))

try:
    while True:
        servo.min()
        sleep(0.5)
        servo.mid()
        sleep(0.5)
        servo.max()
        sleep(0.5)
except KeyboardInterrupt:
    print("keyboard interrupt")
