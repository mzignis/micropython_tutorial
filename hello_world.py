import machine
import time

pin = machine.Pin(5, machine.Pin.OUT)

while True:
    pin.on()
    time.sleep(0.5)
    pin.off()
    time.sleep(0.5)