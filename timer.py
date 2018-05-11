import time
import RPi.GPIO as GPIO

 
red = 16 #pin numbers to match LED legs  
green = 20  
blue = 21 

GPIO.setwarnings(False)
GPIO.setmode(DPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

rpwm = GPIO.PWM(red, 60)
gpwm = GPIO.PWM(green, 60)
bpwm = GPIO.PWM(blue, 60)

rpwm.start(0)
gpwm.start(0)
bpwm.start(0)



constant = 1
j = 1
def on(constant):
    rpwm.ChangeDutyCycle(0)
    gpwm.ChangeDutyCycle(0)
    bpwm.ChangeDutyCycle(0)
    for i in range (0,24):
        rpwm.ChangeDutyCycle(i*4)
        time.sleep(constant)
    return

def offShort(constant):
    rpwm.ChangeDutyCycle(0)
    gpwm.ChangeDutyCycle(0)
    bpwm.ChangeDutyCycle(0)
    for i in range (0,3):
        bpwm.ChangeDutyCycle(i*20)
        time.sleep(constant)
    return

def offLong(j, constant):
    rpwm.ChangeDutyCycle(0)
    gpwm.ChangeDutyCycle(0)
    bpwm.ChangeDutyCycle(0)
    for i in range (0,30):
        gpwm.ChangeDutyCycle(i*3)
        if i % 3 == 0:
            pwm.ChangeDutyCycle((i)+1)
        time.sleep(constant)
    return

def main():
  for i in range(0,2):
      on(constant)
      offShort(constant)
  on(constant)
  offLong(j, constant)
  
if __name__== "__main__":
  main()
