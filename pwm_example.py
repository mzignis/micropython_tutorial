import machine
import time

duty = 0
direction = 1

while True:
    pwm = machine.PWM(machine.Pin(5), freq=20000, duty=duty)
    duty += 1 * direction
    if duty == 1023 or duty == 0:
        direction *= -1
    time.sleep(0.001)

