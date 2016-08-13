import RPi.GPIO as GPIO
import time

port0 = 3
port1 = 5
ports = [port0, port1]

def set_ports():
    GPIO.setmode(GPIO.BCM)
    for port in ports:
        GPIO.setup(port, GPIO.OUT)

def start_port(port):
    GPIO.output(port, GPIO.LOW)
    print "low"
    time.sleep(1)
    GPIO.output(port, GPIO.HIGH)
    print "high"

    
set_ports()
start_port(3)
time.sleep(1)
print "off"