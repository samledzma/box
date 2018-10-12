import RFID
import time

run = True
rdr = RFID.RFID()
util = rdr.util()
util.debug = False

while run:
	(error, data) = rdr.request()
	(error, uid) = rdr.anticoll()
	print len(uid)
	if(len(uid)>0):
		i = 0
		u = []
		for x in uid:
			u[i] = '{0:08b}'.format(x)
			i+=1
		print str(u)
	#print str(uid)
	#time.sleep(1)