import RFID
import time


rdr = RFID.RFID()
util = rdr.util()
util.debug = False


(error, data) = rdr.request()
(error, uid) = rdr.anticoll()
print len(uid)
if(len(uid)>0):
	util.auth(rdr.auth_b, [0x74, 0x00, 0x52, 0x35, 0x00, 0xFF])
	util.rewrite(4, [0x00, 0x00, 0x00, 0x00, 0x00, 0x01])
	util.deauth()