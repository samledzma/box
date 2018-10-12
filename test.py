
import smbus
import time
import datetime
import sys
import threading
import p2
import requests
import json
import RFID
#import pykeypi as teclado
import pantalla
import SimpleMFRC522

import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

import serial

ser = serial.Serial(
    port='/dev/serial0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
           )
counter=0

#ser.write('OPEN|12')
#print('Enviado OPEN|12')

bus = smbus.SMBus(1)
msgToStations = list()
msgToScreen = list()

def writeNumber(adr,value):
    bus.write_byte(adr, value)
    return -1

def readNumber(adr):
    number = bus.read_byte(adr)
    return number

def reset_screen():
    msgToScreen.append("RESET\nRESET")
    p2.lcd_init()

def print_screen(text,line):
    msgToScreen.append(text+"\n"+str(line))

def interprete(com):
    msg = com
    com = com.split("|")
    print com
    if com[0] == "OPEN":
        print "Debe abrir..."
        msgToStations.append(msg)
        reset_screen()
        print_screen(" Listo ",1)
        print_screen(" Toma la bici 1 ",2)
        time.sleep(5)
        print_screen("                ",1)
        print_screen("                ",2)

def login():
    while True:
        print_screen("   Bienvenido   ",1)
        print_screen("                ",2)
        time.sleep(0.005)
        try:
            id, text = reader.read()
            #print(id)
            #print(text)
            interprete("OPEN|14")
            time.sleep(0.5)
        finally:
            GPIO.cleanup()
        '''rdr = RFID.RFID()
        util = rdr.util()
        util.debug = False
        (error, data) = rdr.request()
        if not error:
            print "\nDetected: " + format(data, "02x")

        (error, uid) = rdr.anticoll()
        if not error:
            util.set_tag(uid)
            util.auth(rdr.auth_a, [0x12, 0x34, 0x56, 0x78, 0x96, 0x92])
            info = util.read_out_data(4)
            util.deauth()
            if(info!=False):
                print "Tarjeta detectada" + str(info)
                tecla_pressionada = teclado.keypad()
                teclado.print_msg("Ingrese NIP...")
                reset_screen()
                print_screen(" Ingresa tu NIP ",1)
                print_screen("                ",2)
                espera = True
                tecleos = 0
                nip = ""
                while espera:
                    if str(tecla_pressionada.get_key()):
                        sys.stdout.flush()
                        t = tecla_pressionada.last_key()
                        print t
                        print str(datetime.datetime.now())
                        nip += str(t)
                        tecleos+=1
                        if(tecleos == 1):
                            print_screen("      *         ",2)
                        if(tecleos == 2):
                            print_screen("      **        ",2)
                        if(tecleos == 3):
                            print_screen("      ***       ",2)
                        if(tecleos == 4):
                            espera = False
                            print_screen("   PROCESANDO   ",1)
                            print_screen("   SOLICITUD    ",2)
                            #enviar_server({"mensaje":"Tarjeta detectada : "+str(info),"NIP":nip})
			    interprete("OPEN|1")
                teclado.exit()
            time.sleep(0.0001)'''

def scanner_estaciones():
    i=1
    t=""
    line={}
    line["1"]=p2.LCD_LINE_1
    line["2"]=p2.LCD_LINE_2
    while True:
        if len(msgToScreen) > 0:
            t=msgToScreen.pop(0).split("\n")
            if(t[0]=="RESET"):
                p2.lcd_init()
            else:
                p2.lcd_string(t[0],line[t[1]])
        if len(msgToStations) > 0:
            t=msgToStations.pop(0)
            escribir_estacion(1,t)
            print_there(1, 55, "                                                       ")
            print_there(1, 55, "-> "+t)
        else:
            print_there(i, 55, "                                                       ")
            recibe_estacion = leer_estacion(i)
            #print_there(i, 55, "<- "+recibe_estacion)

            i+=1
            if i > 10:
                i=1
        time.sleep(0.008)

def leer_estacion(adr):
    hadr=getHexAdr(adr)
    try:
        escribir_estacion(adr,"REQ|"+str(adr))
        leer = 0
        texto=""
        while leer < 50:
            x = readNumber(hadr)
            if x == 10:
                    break
            texto+=chr(x)
            leer+=1
        return texto
    except IOError as e:
        #print e
        return "ERROR|CONNECTION_PROBLEM|"+str(adr);

def escribir_estacion(adr,message):
    print "Enviando mensaje --> "
    print message
    hadr=getHexAdr(adr)
    try:
<<<<<<< HEAD
        ser.write(message+'*')
        chars = []
=======
        '''chars = []
>>>>>>> 2e9e4f33ef2913dedab95078bb6679b2063aac53
        for c in message:
                writeNumber(hadr,ord(c))
        writeNumber(hadr,0)
        #print "SEND >> ", message
        return 0'''
	ser.write(message)
    except IOError as e:
        #print e
        return "ERROR|CONNECTION_PROBLEM|"+str(adr);

def getHexAdr(adr):
    return int('0x'+str(10+adr),0)

def print_there(x, y, text):
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
    sys.stdout.flush()


threads = list()
t1 = threading.Thread(target=login)
threads.append(t1)
t1.start()
t2 = threading.Thread(target=scanner_estaciones)
threads.append(t2)
t2.start()
reset_screen()

while True:
    time.sleep(0)
<<<<<<< HEAD
    texto = raw_input("SEND COMMAND: ")
    msgToStations.append(texto)
    ser.write(texto)
=======
    msgToStations.append(raw_input("SEND COMMAND: "))
    ser.write('---TEST---')
>>>>>>> 2e9e4f33ef2913dedab95078bb6679b2063aac53
