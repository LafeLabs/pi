## [back up to main pi scroll](../)

[open arduino class](https://github.com/LafeLabs/openarduino)

[dataloggercode/](dataloggercode/)

## Arduino Actions

 - monitor and log water level
 - measure temperature and 



how to do the tar ball thing to get a later version of arduino which has the plotting

```
cd ~
cd Downloads
ls
tar -xf arduino-####-linuxarm.tar.xz
sudo mv arduino-#### /opt
sudo /opt/arduino-####/install.sh
```

[https://www.raspberrypi-spy.co.uk/2020/12/install-arduino-ide-on-raspberry-pi/](https://www.raspberrypi-spy.co.uk/2020/12/install-arduino-ide-on-raspberry-pi/)

trying to get data from the arduino to python


### batteryvoltage.ino

```
#include <ArduinoJson.h>

int x;
float voltsperpoint = 12.73/428.0;//based on measuring with DVM fully charged battery
float v = 0.0;

void setup() {
 Serial.begin(9600);
}

void loop() {

  x = analogRead(A1);
  v = voltsperpoint*x;//convert to volts
  DynamicJsonDocument measurement(200);
  measurement["x"] = x;
  measurement["v"] = v;
  serializeJson(measurement, Serial);
  Serial.println();

}
```

### batteryvoltage.py

```
import serial
import json
import time
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
```




