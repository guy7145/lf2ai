import socket
import time
import os
import subprocess

client = None
def press_and_release(key):
	client.send("{0}{1}".format(1,chr(key)).encode())
	
def press(key):
	client.send("{0}{1}".format(2,chr(key)).encode())

def release(key):
	client.send("{0}{1}".format(3,chr(key)).encode())

def long_press(key,timing):
	press(key)
	time.sleep(timing)
	release(key)
	
def press_enter(timing):
	long_press(0x0D,timing)

def press_shift(timing):
	long_press(0x10,timing)	
	
def press_ctrl(timing):
	long_press(0x11,timing)
		
def press_left(timing):
	long_press(0x25,timing)

def press_up(timing):
	long_press(0x26,timing)

def press_right(timing):
	long_press(0x27,timing)

def press_down(timing):
	long_press(0x28,timing)	
	
	
def init():	
	global client
	ls_output=subprocess.Popen(["fast_keys.exe"], stdout=subprocess.PIPE)
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect(('127.0.0.1', 8888))		
		
if __name__ == "__main__":
	init()
	print("hiii")
	time.sleep(5) 
	while(True):
		press_and_release(0x25)
		time.sleep(1) 
	press_and_release(0x26)
	time.sleep(1) 
	press_and_release(0x27)
	time.sleep(1) 
	press_and_release(0x28)