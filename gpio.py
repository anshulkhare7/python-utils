import RPi.GPIO as GPIO
import argparse
from time import sleep

def main(period):
    
    #Assign Pins
    blower_pin_1=40
    blower_pin_2=38
    feeder_pin_1=37
    unused_board_pins = (3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 18, 19, 21, 22, 23, 24, 26, 29, 31, 32, 33, 35, 36, 37, 38)
    relay_pins = (blower_pin_1, blower_pin_2, feeder_pin_1)

    #Setup GPIO
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(unused_board_pins, GPIO.OUT, initial=True)
    GPIO.setup(relay_pins, GPIO.OUT, initial=True)

    #Turn on PINs
    GPIO.output(blower_pin_1, False)
    GPIO.output(blower_pin_2, False)
    
    sleep(int(period))
    
    #Turn off PINs
    GPIO.output(blower_pin_1, True)
    GPIO.output(blower_pin_2, True)

if __name__=="__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--period", required=True, type=str, help="Time in seconds to keep the pin On")
    args = vars(ap.parse_args())
    period = args["period"]
    main(period)
