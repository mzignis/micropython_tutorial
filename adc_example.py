import machine
import time

adc = machine.ADC(machine.Pin(36))

while True:
    print(adc.read())
    time.sleep(1)
    