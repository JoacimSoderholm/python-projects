#!/usr/bin/python
import threading
import random
import time

BOARD = "board"
BCM = "bcm"
OUT = "out"
IN = "in"

c1 = 1
c2 = 1
c3 = 1
c4 = 1
c5 = 1
c6 = 1
c7 = 1
c8 = 1
c9 = 1
c10 = 1
c11 = 1
c12 = 1
c13 = 1
c14 = 1
c15 = 1
c16 = 1
c17 = 1
c18 = 1
c19 = 1
c20 = 1

thread = 0

def output(pin,value):
	print(pin, ":", value)
	pass
	
def input(pin):
	if(pin == 16):
		return c16
	if(pin == 12):
		return c12
	pass
	
def setmode(mode):
	print(mode)
	pass
	
def setup(pin, mode):
	print(pin, ":", mode)
	if(mode == IN):
		if(thread != 0):
			thread.stop()
		t = threading.Thread(target=randomizer, args=(pin,))
		t.daemon = True
		t.start()
	pass
	
def cleanup():
	print("clean-up")
	
	pass
	
def setwarnings(value):
	print(value)
	pass

def randomizer(pin):
	while True:
		time.sleep(2)
		if(pin == 16):
			global c16
			c16 = random.randint(0, 1)
		if(pin == 12):
			global c12
			c12 = random.randint(0, 1)
#End