from machine import Pin
import utime
import neopixel

np = neopixel.NeoPixel(machine.Pin(16), 1)

trigger = Pin(12, Pin.OUT)
echo = Pin(11, Pin.IN)

def ultradistance():

    np[0] = (0, 0, 20)
    np.write()

    trigger.low()
    utime.sleep_us(2)

    trigger.high()
    utime.sleep_us(5)
    trigger.low()

    while echo.value() == 0:
       signaloff = utime.ticks_us()
    while echo.value() == 1:
       signalon = utime.ticks_us()

    timepassed = signalon - signaloff

    distance = round(((timepassed * 0.0343) / 2), 1)
    print(distance)
    
    np[0] = (0, 0, 0)
    np.write()

while True:
   ultradistance()
   utime.sleep(0.25)