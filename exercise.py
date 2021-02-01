import machine
import time

button = machine.Pin(26, machine.Pin.IN)
pwm = machine.PWM(machine.Pin(25), freq=20000, duty=0)
adc = machine.ADC(machine.Pin(36))


while True:
    duty = int(adc.read() / 4)
    pwm.duty(duty)
    
    if not button.value():
        print('DUTY: {}%'.format(duty / 1024 * 100))
        time.sleep(0.25)
    else: 
        time.sleep(0.05)
