import serial
import json
import time


for index in range(10):
    ser = serial.Serial('/dev/ttyUSB0', 9600)
    data = ""
    for x in range(4):
        data += ser.readline()
    cleandatastring = data.decode('latin1')
    dataarray = cleandatastring.split('\n')
    secondelement = dataarray[1];
    jsondata = json.loads(secondelement)
    timestamp = round(time.time())
    jsondata['timestamp'] = timestamp
    jsondatastring = json.dumps(jsondata) + ",\n"
    file = open("datafile.txt", "a")
    file.write(jsondatastring)
    file.close()
    #print(jsondatastring)
    ser.close()
    time.sleep(10)