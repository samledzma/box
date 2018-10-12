#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal

continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
LECTOR = MFRC522.MFRC522()

# Welcome message
print "Welcome to the MFRC522 data read example"
print "Press Ctrl-C to stop."

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    
    # Scan for cards    
    (status,TagType) = LECTOR.MFRC522_Request(LECTOR.PICC_REQIDL)

    # If a card is found
    if status == LECTOR.MI_OK:
        print "Card detected"
    
    # Get the UID of the card
    (status,uid) = LECTOR.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == LECTOR.MI_OK:

        # Print UID
        print "Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])
    
        # This is the default key for authentication
        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
        
        # Select the scanned tag
        LECTOR.MFRC522_SelectTag(uid)

        # Authenticate
        status = LECTOR.MFRC522_Auth(LECTOR.PICC_AUTHENT1A, 8, key, uid)

        # Check if authenticated
        if status == LECTOR.MI_OK:
            #LECTOR.MFRC522_Read(8)
            LECTOR.MFRC522_DumpClassic1K(key, uid)
            LECTOR.MFRC522_StopCrypto1()
        else:
            print "Authentication error"

