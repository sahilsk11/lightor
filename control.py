import RPi.GPIO as GPIO
import time
import datetime

class relay_control:
    
    def __init__(self, ports):
        self.ports = ports

    def set_ports(self):
        GPIO.setmode(GPIO.BCM)
        for port in self.ports:
            GPIO.setup(port, GPIO.OUT)
    
    def start_port(self,port):
        GPIO.output(port, GPIO.LOW)
        print "on"
    
    def stop_port(port):
        GPIO.output(port, GPIO.HIGH)
        print "off"
    
    def ports_on():
        for port in self.ports:
            start_port(port)
            time.sleep(1)

if (__main__ == "__name__"):
    set_ports()
    ports_on()
    time.sleep(5)
    stop_port(3)
    stop_port(18)
    time.sleep(1)
    print "finished at " + str(datetime.datetime.now())