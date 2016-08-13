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
    time.sleep(1)
    GPIO.output(port, GPIO.HIGH)

    
set_ports()
start_port(3)
time.sleep(3)
start_port(5)
time.sleep(3)
time.sleep(3)
GPIO.clean_up()