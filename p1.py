import RFID
import time

def login():
    rdr = RFID.RFID()
    util = rdr.util()
    util.debug = False
    while True:
        (error, data) = rdr.request()
        if not error:
            print "\nDetected: " + format(data, "02x")

        (error, uid) = rdr.anticoll()
        if not error:
            util.set_tag(uid)
            util.auth(rdr.auth_a, [0x12, 0x34, 0x56, 0x78, 0x96, 0x92])
            info = util.read_out_data(4)
            if(info!=False):
                print str(info)
            util.deauth()
            time.sleep(0.0001)

login()