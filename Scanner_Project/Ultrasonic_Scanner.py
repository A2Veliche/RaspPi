# import RPi.GPIO as GPIO
from gpiozero import DistanceSensor
from ServoControl import Servo
import datetime, time

servo_pin = 24
echo_pin = 17
trigger_pin = 4
time_between_turns = 0.2

scan_deg_list = [-180, -90, 0, 90, 180]
dist_list = []

myUlt = DistanceSensor(echo=echo_pin, trigger=trigger_pin)
myS = Servo(servo_pin, True)

my_in = str(input("Align distance sensor towards a wall \nEnter 4 when ready > "))

for i in scan_deg_list:
    myS.turnToDeg(i, 0.5)
    time.sleep(time_between_turns)
    dist_list.append(myUlt.distance)
    time.sleep(time_between_turns)

compressed_vals = list(zip(scan_deg_list, dist_list))

with open("Scan_Data.txt", 'w') as dataFile:
    date_time = datetime.datetime.now()
    dataFile.write("scan at time: {}".format(date_time))
    for i in compressed_vals:
        dataFile.write("\n Reading at {} degrees -> {} cm".format(i[0], i[1]))
    dataFile.close()

print("Done! \n")
