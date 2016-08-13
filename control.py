import RPi.GPIO as GPIO
import time
import datetime

port0 = 3
port1 = 5
ports = [port0, port1]

def set_ports():
    GPIO.setmode(GPIO.BCM)
    for port in ports:
        GPIO.setup(port, GPIO.OUT)

def start_port(port):
    GPIO.output(port, GPIO.LOW)
    print "on"

def stop_port(port):
    GPIO.output(port, GPIO.LOW)
    print "off"
    
set_ports()
start_port(3)
time.sleep(1)
stop_port(3)
print "finished at " + str(datetime.datetime.now())