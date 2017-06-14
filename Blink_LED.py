import time
import RPi.GPIO as GPIO
#import logging as lg


def get_input(string, str_type):
    while True:
        my_in = eval(str(input(string)))
        if isinstance(my_in, str_type):
            return my_in
        else:
            print("Not a valid input. Type required" + str(str_type))


blinkPin = 24
delay_time = get_input("Blink delay time (in seconds) \n>> ", float)
blink_times = get_input("Input blink times \n>> ", int)

GPIO.setmode(GPIO.BCM)
GPIO.setup(blinkPin, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)

print("SETUP: times {}; delay {}; pin number {}".format(blink_times, delay_time, blinkPin))

i = True
x = 0

while x < blink_times * 2:
    if i:
        GPIO.output(blinkPin, GPIO.HIGH)
        stat = "high"
    else:
        GPIO.output(blinkPin, GPIO.LOW)
        stat = "low"
    print("Pin#{} status: {} {}".format(blinkPin, "OUT", stat))
    time.sleep(delay_time)
    i = not i
    x += 1

print("Finished blinking sequence\n")
GPIO.cleanup()
