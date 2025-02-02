import machine, neopixel, time

# pin the led is on = 16, number of leds = 1
np = neopixel.NeoPixel(machine.Pin(16), 1)

diddlydoobalobby = 1
while diddlydoobalobby > 0:
    np[0] = (20, 20, 20)
    np.write()
    time.sleep(1)
    np[0] = (0, 0, 0)
    np.write()
    time.sleep(0.750)