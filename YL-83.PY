# raindrop sensor DO connected to GPIO18
# HIGH = no rain, LOW = rain detected
from time import sleep
from gpiozero import Buzzer, InputDevice

no_rain = InputDevice(17)
 
def alertfunc(iterations):
    for x in range(iterations):
        print("Deu boa, detectamos chuva")
 
while True:
    if not no_rain.is_active:
        print("It's raining!!")
        alertfunc(3)
    sleep(1)