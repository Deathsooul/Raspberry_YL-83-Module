# raindrop sensor DO connected to GPIO18
# HIGH = no rain, LOW = rain detected
from time import sleep
from gpiozero import InputDevice

no_rain = InputDevice(17)
 
def alertfunc(iterations):
    for x in range(iterations):
        print("Aleluia...")
 
while True:
    if not no_rain.is_active:
        print("It's raining man!!")
        alertfunc(3)
    sleep(1)