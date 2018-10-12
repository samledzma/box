#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal


LECTOR = MFRC522.MFRC522()
(status,TagType) = LECTOR.MFRC522_Request(LECTOR.PICC_REQIDL)
if status == LECTOR.MI_OK:
    print "Card detected"
(status,uid) = LECTOR.MFRC522_Anticoll()
if status == LECTOR.MI_OK:
    print "Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])
    key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
    LECTOR.MFRC522_SelectTag(uid)
    status = LECTOR.MFRC522_Auth(LECTOR.PICC_AUTHENT1A, 8, key, uid)
    if status == LECTOR.MI_OK:
        #LECTOR.MFRC522_Read(8)
        LECTOR.MFRC522_DumpClassic1K(key, uid)
        LECTOR.MFRC522_StopCrypto1()
    else:
        print "Authentication error"