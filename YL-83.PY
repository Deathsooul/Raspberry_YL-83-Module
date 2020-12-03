from time import sleep          
import RPi.GPIO as GPIO         
 
GPIO.setmode(GPIO.BCM)          
INPUT_PIN = 17           
GPIO.setup(INPUT_PIN, GPIO.IN)           

while True: 
           if (GPIO.input(INPUT_PIN) == True): # Physically read the pin now
                    print(GPIO.input(INPUT_PIN))
           else:
                    print('0')
           sleep(1);           