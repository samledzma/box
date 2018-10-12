#'''
import RFID
import time

rdr = RFID.RFID()
util = rdr.util()
#'''

def leer_sector():
	print "Inserte SECTOR + _ + A|B + KEY separado por espacios"
	read_info=raw_input("INSERTE: ")
	info = read_info.split(" ")
	print "Sector : " + info[0]
	print "Tipo   : " + info[1]
	print "Key    : " + str(info[2:])
	
	if(info[1]=="a"):
		tipo = rdr.auth_a #1
		pwd = [0x12, 0x34, 0x56, 0x78, 0x96, 0x92]
	else:
		tipo = rdr.auth_b #1
		pwd = [0x74, 0x00, 0x52, 0x35, 0x00, 0xFF]
	#pwd = [hex(int(info[2],16)), hex(int(info[3],16)), hex(int(info[4],16)), hex(int(info[5],16)), hex(int(info[6],16)), hex(int(info[7],16))]
	print str(pwd)
#'''
	while True:
		(error, data) = rdr.request()
		(error, uid) = rdr.anticoll()
		if not error:
			util.set_tag(uid)
			util.auth(tipo, pwd)
			util.read_out(4)
			util.deauth()
#'''
	

while True:
	print "1 => Leer Tarjeta"
	print "2 => Restaurar sector de tarjeta a Fabrica"
	print "3 => Colocar valores en sector de Tarjeta"
	action=raw_input("OPCION: ")
	if action == "1":
		leer_sector()
	if action == "2":
		print "Restaurar sector de tarjeta"
	if action == "3":
		print "Colocar valores en sector de Tarjeta"
