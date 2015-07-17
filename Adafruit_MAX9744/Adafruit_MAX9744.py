#!/usr/bin/python

# Adafruit_MAX9744.py

import RPi.GPIO as GPIO
from Adafruit_I2C import Adafruit_I2C

# Address of the amplifier
MAX9744_I2CADDR = 0x4B
#MAX9744_I2CADDR = 0x4A
#MAX9744_I2CADDR = 0x49

# GPIO pin number of mute pin
MUTE_PIN = 17

# GPIO pin number of shutdown pin
SHUTDOWN_PIN = 27

class Adafruit_MAX9744 :
    # Constructor
    def __init__(self, address=MAX9744_I2CADDR):
        # Setup i2c
        self.i2c = Adafruit_I2C(address)
        self.address = address
        
        # Setup GPIO for Shutdown and Mute pins
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(SHUTDOWN_PIN, GPIO.OUT)
        GPIO.setup(MUTE_PIN, GPIO.OUT)
        GPIO.output(SHUTDOWN_PIN, True);
        GPIO.output(MUTE_PIN, True);

    # Write the volume level to the amplifier
    def set_volume(self, value):
        if value > 63:
            value = 63
        if value < 0:
            value = 0
        self.i2c.write8(0x00, value)

    # Mute the amplifier
    def set_mute(self, value):
        if value == True:
            GPIO.output(MUTE_PIN, False)
        if value == False:
            GPIO.output(MUTE_PIN, True)

    # Shutdown the amplifier
    def set_shutdown(self, value):
        if value == True:
            GPIO.output(SHUTDOWN_PIN, False)
        if value == False:
            GPIO.output(SHUTDOWN_PIN, True)

    # Cleanup the GPIO pins when closing the program
    def cleanup(self):
        GPIO.cleanup()


if __name__ == '__main__':
    
    def menu():
        print
        print ('Commands:')
        print ('  + to increase volume')
        print ('  - to decrease volume')
        print ('  m to mute amplifier')
        print ('  u to unmute amplifier')
        print ('  d to shutdown amplifier')
        print ('  s to startup amplifier')
        print ('  h to show this menu')
        print ('  q to quit')
        print
    
    amp = Adafruit_MAX9744()
    thevol = 31
    c='0'
    print
    print ('Adafruit MAX9744 i2c Volume Control Demo')
    menu()
    
    amp.set_volume(thevol)
    print ('Setting volume to ' + str(thevol))
    print

    # Read in + and - characters to set the volume.
    while not (c == 'q'):
        c = raw_input('Enter command: ')
    
        # increase
        if (c == '+'):
            thevol=thevol+1
            print ('Setting volume to ' + str(thevol))
            amp.set_volume(thevol)
        
        # decrease
        elif (c == '-'):
            thevol=thevol-1
            print ('Setting volume to ' + str(thevol))
            amp.set_volume(thevol)
    
        # mute
        elif (c == 'm'):
            amp.set_mute(True)
            print ('Mute is on')
    
        # unmute
        elif (c == 'u'):
            amp.set_mute(False)
            print ('Mute is off')
    
        # shutdown
        elif (c == 'd'):
            amp.set_shutdown(True)
            print ('Amplifier is off')
    
        # startup
        elif (c == 's'):
            amp.set_shutdown(False)
            print ('Amplifier is on')

        # menu
        elif (c == 'h'):
            menu()

        # ignore anything else
    
        if (thevol > 63):
            thevol = 63
        if (thevol < 0):
            thevol = 0
    
    # Close program and cleanup GPIO
    amp.cleanup()
