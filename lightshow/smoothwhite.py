import machine, neopixel, time

# defines `np`, pin the led is on = 16, number of leds = 1
np = neopixel.NeoPixel(machine.Pin(16), 1)

diddlydoobalobby = 1
while diddlydoobalobby > 0:
    for blueval in range(200):
        np[0] = (0, 0, blueval)
        np.write()
        time.sleep(0.02)
    for redval in range(200):
        np[0] = (redval, 0, 200)
        np.write()
        time.sleep(0.02)
    for greenval in range(200):
        np[0] = (200, greenval, 200)
        np.write()
        time.sleep(0.02)