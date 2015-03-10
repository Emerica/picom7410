#!/usr/bin/python
import serial
debug = 0

ser = serial.Serial('/dev/ttyUSB0', 19200) 

def ic7410_get_frequency():
    s = ser.write("\xfe\xfe\x80\x00\x03\xfd")

def ic7410_show_mode(byte):
    if byte == "\x00":
        print "Mode: LSB"
    elif byte == "\x01":
        print "Mode: USB"
    elif byte == "\x02":
        print "Mode: AM"
    elif byte == "\x03":
        print "Mode: CW"
    elif byte == "\x04":
        print "Mode: RTTY"
    elif byte == "\x05":
        print "Mode: FM"
    elif byte == "\x06":
        print "Mode: Wide FM"
    elif byte == "\x07":
        print "Mode: CW-R"
    elif byte == "\x08":
        print "Mode: RTTY-R"

def ic7410_show_filter(byte):
    if byte == "\x01":
        print "Filter: 1"
    elif byte == "\x02":
        print "Filter: 2"
    elif byte == "\x03":
        print "Filter: 3"


def ic7410_show_frequency(cmd):
    cmd = ''.join(cmd).encode('hex')
    print cmd[10:11]+"."+cmd[11:12]+cmd[8:9]+cmd[9:10] + "." + cmd[6:7]+ cmd[7:8] + cmd[4:5] + "." + cmd[5:6]+ cmd[2:3]  + "Ghz"

def ic7410_read():
    s = ""
    while s != "\xfe":
        if debug : print "waiting for sync...." + s.encode('hex')
        s = ser.read()
    if ser.read() == "\xfe":
        if debug : print "synced, packet info :"
        i = 0
        command = []
        while s != "\xfd":
            s = ser.read()
            if  i == 0 :
                if debug : print "TO:"+ s.encode('hex')
            elif i == 1:
                if debug : print "FROM:"+ s.encode('hex')
            else:
                command.append(s)
            i +=1
        command.pop()
        return command

read = 1
ic7410_get_frequency()
while read!=0:
    cmd = ic7410_read()
    if cmd[0] == "\x00":
        ic7410_show_frequency(cmd)
    elif cmd[0] == "\x01":
        ic7410_show_mode(cmd[1])
        ic7410_show_filter(cmd[2])
    elif cmd[0] == "\x03":
        ic7410_show_frequency(cmd)
    else:
       print "Unknown Command (" +cmd[0].encode('hex')+ "), mail blendz@shaw.ca"
ser.close()

