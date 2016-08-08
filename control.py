import RPi.GPIO as GPIO
from time import sleep

port0 = 3
port1 = 5
ports = [port0, port1]

def set_ports():
    for port in ports:
        GPIO.setup(port, GPIO.OUT)

def start_port(port):
    GPIO.output(port, GPIO.HIGH)

def stop_port(port):
    GPIO.output(port, GPIO.LOW)
    
set_ports()
start_port(3)
time.sleep(3)
stop_port(port)
time.sleep(3)