import RPi.GPIO as GPIO  
import time  
  
GPIO.setmode(GPIO.BCM)  
input_pin = 17  
GPIO.setup(input_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  
  
try:  
    while True:  
        pin_state = GPIO.input(input_pin)  
        print("Pin state:", pin_state)  
        time.sleep(1)  
  
except KeyboardInterrupt:  
    print("Stopping...")  
  
finally:  
    GPIO.cleanup()  
