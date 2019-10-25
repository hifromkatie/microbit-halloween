from microbit import *
import neopixel

np = neopixel.NeoPixel(pin0, 1)
G=0
R=0
B=0

while True:
    #G,R,B
    pos = accelerometer.current_gesture()
    if (pos=="left"):
        display.show(Image("90000:90000:90000:90000:90000"))
    elif (pos=="right"):
        display.show(Image("00009:00009:00009:00009:00009"))
    else:
        display.show(Image("00900:00900:00900:00900:00900"))
    
    if button_a.is_pressed():
        if (pos=="left"):
            if (R<255):
              R=R+1
        elif (pos=="right"):
            if (B<255):
              B=B+1
        else:
            if (G<255):
                G=G+1
    elif button_b.is_pressed():
        if (pos=="left"):
            if (R>0):
                R=R-1
        elif (pos=="right"):
            if (B>0):
                B=B-1
        else:
            if (G>0):
                G=G-1
    np[0]= (G,R,B)
    np.show()