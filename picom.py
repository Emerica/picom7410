#!/usr/bin/python
import serial
debug = 0

ser = serial.Serial('/dev/ttyUSB0', 19200) 

def ic7410_get_frequency():
    s = ser.write("\xfe\xfe\x80\x00\x03\xfd")


def read_7410():
    s = ""
    while s != "fe":
        #print "waiting for sync...." + s
        s = ser.read().encode('hex')
    if ser.read().encode('hex') == "fe":
        #print "synced, packet info :"
        i = 0
        command = ""
        while s != "fd":
            s = ser.read().encode('hex')
            if  i == 0 :
                if debug : print "TO:"+s
            elif i == 1:
                if debug : print "FROM:"+s
            else:
                command = command + s
            i +=1
        return command[:-2]

read = 1
ic7410_get_frequency()
while read!=0:
    cmd = read_7410()
    if cmd == "010201":
       print "Filter 1 AM"
    elif cmd == "010202":
       print "Filter 2 AM"
    elif cmd == "010203":
       print "Filter 3 AM"
    elif cmd[:2] == "03":
       print cmd[10:11]+"."+cmd[11:12]+cmd[8:9]+cmd[9:10] + "." + cmd[6:7]+ cmd[7:8] + cmd[4:5] + "." + cmd[5:6]+ cmd[2:3]  + "Ghz"
    elif cmd[:2] == "00":
       print cmd[10:11]+"."+cmd[11:12]+cmd[8:9]+cmd[9:10] + "." + cmd[6:7]+ cmd[7:8] + cmd[4:5] + "." + cmd[5:6]+ cmd[2:3]  + "Ghz"
    else:
       print "Unknown Command (" +cmd+ "), mail blendz@shaw.ca"
ser.close()

