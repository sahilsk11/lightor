import RPi.GPIO as GPIO
import time
import datetime

port0 = 3
port1 = 18
ports = [port0, port1]

def set_ports():
    GPIO.setmode(GPIO.BCM)
    for port in ports:
        GPIO.setup(port, GPIO.OUT)

def start_port(port):
    GPIO.output(port, GPIO.LOW)
    print "on"

def stop_port(port):
    GPIO.output(port, GPIO.HIGH)
    print "off"

def ports_on():
    for port in ports:
        start_port(port)

set_ports()
ports_on()
time.sleep(1)
stop_port(3)
stop_port(5)
time.sleep(1)
print "finished at " + str(datetime.datetime.now())