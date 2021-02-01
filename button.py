import machine
import time

cnt = 0
button = machine.Pin(5, machine.Pin.IN)
while True:
	if not button.value():
		cnt += 1
		print('Button clicked {} time!'.format(cnt))
		time.sleep(0.5)

