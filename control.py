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
    GPIO.output(port, GPIO.HIGH)

def stop_port(port):
    GPIO.output(port, GPIO.LOW)
    
set_ports()
start_port(3)
time.sleep(3)
stop_port(port)
time.sleep(3)