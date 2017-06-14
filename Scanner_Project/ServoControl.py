import time, numpy
import wiringpi as wp


class Servo:
    def __init__(self, pwm_pin, turn_360=True):
        self.pin = pwm_pin
        self.turn_360 = turn_360
        self.degLog = []
        self.setup()

    def setup(self):
        wp.pinMode(self.pin, wp.GPIO.PWM_OUTPUT)
        wp.pwmSetMode(wp.GPIO.PWM_MODE_MS)
        wp.pwmSetClock(192)
        wp.pwmSetRange(2000)

    def turnToDeg(self, degrees, travel_time):
        self.degLog.append(degrees)
        if self.turn_360:
            degrees = numpy.clip(degrees, -180, 180)
        else:
            degrees = numpy.clip(degrees, -90, 90)
        time_ms = 1.5 + 0.5 * degrees / 90
        delay = 0.02
        i = 0
        while i < travel_time / delay:
            wp.pwmWrite(self.pin, int(time_ms * 10))
            time.sleep(delay)
            i += 1

if __name__ == "__main__":
    myS = Servo(8, True)
    myS.turnToDeg(30, 0.1)

