from gpiozero import Servo
from time import sleep
import time
import RPi.GPIO as GPIO
import I2C_LCD_driver as driver

RED = 17  #port11
GREEN = 27  #port13

TRIG = 10  #port19
ECHO = 9  #port21

# Dmin = 15
# Dmax = 25

servo = Servo(18)

LCD = driver.lcd()

def setup():
    #GPIO.setmode(GPIO.BOARD)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(RED, GPIO.OUT)
    GPIO.setup(GREEN, GPIO.OUT)
    
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    
def calculerDistance():
    GPIO.output(TRIG, False)
    GPIO.output(TRIG, True)
    time.sleep(0.000001)
    GPIO.output(TRIG, False)
    
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
        
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
        
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17000
    distance = round(distance, 2)
    return distance

def decideOpen(distance,free):
    LCD.lcd_clear()
    if(free==0):
        LCD.lcd_display_string("park full",1,2)
        return
    LCD.lcd_display_string("free : "+str(free),2,2)
    if distance <= 8:
        servo.max()
        print("GATE OPEN")
        LCD.lcd_display_string("GO AHEAD!", 1, 2)
        sleep(1)
        GPIO.output(RED, False)
        GPIO.output(GREEN, True)
        sleep(0.5)
        return
    
    if distance >= 8:
        servo.min()
        GPIO.output(RED, True)
        GPIO.output(GREEN, False)
        print("GATE CLOSED")
        
        LCD.lcd_display_string(" CLOSED! ", 1, 2)
        sleep(0.5)
        return

def job(free = 0):
    distance = calculerDistance()
    decideOpen(distance,free)
    
def loop():
    while True:
        job()


def destroy():
    #LCD.lcd_clear()
    GPIO.output(RED, False)
    GPIO.output(GREEN, False)
    GPIO.output(TRIG, False)
    GPIO.cleanup()
    
def main():
    setup() 
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
   
if __name__ == "__main__":
    main()

    



