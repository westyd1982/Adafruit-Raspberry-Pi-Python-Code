#!/usr/bin/python

# Adafruit_MAX9744_Volume_CLI.py

from Adafruit_MAX9744 import Adafruit_MAX9744
import sys, getopt

def main(argv):
    thevol = 31
    mute = False
    shutdown = False
    amp = Adafruit_MAX9744()

    try:
        opts, args = getopt.getopt(argv,"hv:",["volume="])
    except getopt.GetoptError:
        print 'Usage: Adafruit_MAX9744_Volume_CLI.py -v <volume value 0-63>'
        amp.cleanup()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'Usage: Adafruit_MAX9744_Volume_CLI.py -v <volume value 0-63>'
            amp.cleanup()
            sys.exit()
        if opt in ("-v", "--volume"):
            thevol = int(arg)
            amp.set_volume(thevol)
            print
            print ('Setting volume to ' + str(thevol))
            print

    # Cleanup GPIO on exit
    amp.cleanup()

if __name__ == "__main__":
    main(sys.argv[1:])
