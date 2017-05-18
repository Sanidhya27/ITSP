'''
import RPi.GPIO as GPIO
right_motor_1=
right_motor_2=
left_motor_1=
left_motor_2=
'''
def gpio_setup():
	"""Sets the GPIO pins for the two motors"""
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(right_motor_1, GPIO.OUT)
    GPIO.setup(right_motor_2, GPIO.OUT)
    GPIO.setup(left_motor_1, GPIO.OUT)
    GPIO.setup(left_motor_2, GPIO.OUT)
def instructions(command):
	if command=="LEFT":
		"""Set mode to Left"""
    	GPIO.output(right_motor_1, True)
   		GPIO.output(right_motor_2, False)
    	GPIO.output(left_motor_1, False)
    	GPIO.output(left_motor_2, True)
    if command=="RIGHT":	
        """Set mode to Right"""
	    GPIO.output(right_motor_1, False)
	    GPIO.output(right_motor_2, True)
	    GPIO.output(left_motor_1, True)
	    GPIO.output(left_motor_2, False)
	if command=="FORWARD":
		"""Set mode to Forward"""
    	GPIO.output(right_motor_1, True)
   		GPIO.output(right_motor_2, False)
    	GPIO.output(left_motor_1, True)
    	GPIO.output(left_motor_2,False)
    if command=="BACK":	
        """Set mode to Backward"""
	    GPIO.output(right_motor_1, False)
	    GPIO.output(right_motor_2, True)
	    GPIO.output(left_motor_1, False)
	    GPIO.output(left_motor_2, True) 
	if command=="no command":
	    GPIO.output(right_motor_1, False)
	    GPIO.output(right_motor_2, False)
	    GPIO.output(left_motor_1, False)
	    GPIO.output(left_motor_2, False)



		
