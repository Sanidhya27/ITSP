
import RPi.GPIO as GPIO
<<<<<<< HEAD
right_motor_1=17
right_motor_2=22
left_motor_1=19
left_motor_2=13


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.OUT)
a=GPIO.PWM(13,500)
a.start(0)
GPIO.setup(19,GPIO.OUT)
b=GPIO.PWM(19,500)
b.start(0)
GPIO.setup(17,GPIO.OUT)
d=GPIO.PWM(17,500)
d.start(0)
GPIO.setup(22,GPIO.OUT)
c=GPIO.PWM(22,500)
c.start(0)


=======
right_motor_1=
right_motor_2=
left_motor_1=
left_motor_2=
>>>>>>> 25668b80b89e1df32a172012446d6e300992b655

def gpio_setup():
    """Sets the GPIO pins for the two motors"""
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(right_motor_1, GPIO.OUT)
    GPIO.setup(right_motor_2, GPIO.OUT)
    GPIO.setup(left_motor_1, GPIO.OUT)
    GPIO.setup(left_motor_2, GPIO.OUT)

def instructions(command):
   
    print("hi")
    if command=="LEFT":
        """Set mode to Left"""
        print("hi left")
        a.ChangeDutyCycle(0)
        b.ChangeDutyCycle(30)
        c.ChangeDutyCycle(0)
        d.ChangeDutyCycle(70)
    if command=="RIGHT":	
        """Set mode to Right"""
        print("hi right")
        a.ChangeDutyCycle(0)
        b.ChangeDutyCycle(70)
        c.ChangeDutyCycle(0)
        d.ChangeDutyCycle(30)
    if command=="FORWARD":
        """Set mode to Forward"""
        print("hi for")
        a.ChangeDutyCycle(0)
        b.ChangeDutyCycle(54)
        c.ChangeDutyCycle(0)
        d.ChangeDutyCycle(50)
    if command=="BACK":	
        """Set mode to Backward"""
        print("hi back")
        a.ChangeDutyCycle(80)
        b.ChangeDutyCycle(0)
        c.ChangeDutyCycle(80)
        d.ChangeDutyCycle(0)

    if command=="no command":
        a.ChangeDutyCycle(0) #GPIO.output(17, False)
        b.ChangeDutyCycle(0) #GPIO.output(19, False)
        c.ChangeDutyCycle(0) #GPIO.output(27, False)
        d.ChangeDutyCycle(0) #GPIO.output(26, False)



		
