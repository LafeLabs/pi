## [back up to main pi scroll](../)

# Python

## Goals

in the community networking pi server/terminal, we only need python for one thing: recording data down the serial port. that is then all saved as raw json data in a .txt file which is used by p5j javascript into html.  So all we need from python is open file, save file, read serial.  that's it.  we don't need jupyter.  

Hence the goal

 - install python and make sure it's working
 - print hello world get python working
 - run a python script to record data from serial into the log file
 - operate python script in background or on a schedule so that log files are taken over time

Since we are *only* using python to record data from arduino to file, we can destroy this whole repository, eliminate all the robotics and neopixel from arduino, eliminate the shield, so the arduino is just sensors with jumpers, all off the shelf, 

Then we can link to resources, which are matplotlib and w3schools tutorial, and that's it.

### [matplotlib](https://matplotlib.org/)
### [w3schools](https://www.w3schools.com/python/default.asp)


this is how you run pythonfile.py from php, allowing you to update data from browser remotely over apache/geometron:

```
<?php
shell_exec("python3 pythonfile.py");
?>
```

```
#include <ArduinoJson.h>

int x;
float voltsperpoint = 12.46/399;//based on measuring with DVM fully charged battery
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

## Links

 - [codeserver/](codeserver/)
 - [http://localhost](http://localhost)
 - [../](../)
 - [fork.html](fork.html)
 - [readme.html](readme.html)
 - [home](index.html)
 - [editor.php](editor.php)
 - [scrolleditor.html](scrolleditor.html)
 - [set.html](set.html)
 - [dnagenerator.php](dnagenerator.php)
 - [global replicator code link](https://raw.githubusercontent.com/LafeLabs/bioweb/main/php/replicator.txt)
 - [local replicator code link](php/replicator.txt)


matplotlib install:

<pre>
sudo apt install python3-matplotlib
</pre>

[https://matplotlib.org/](https://matplotlib.org/)

[https://www.instructables.com/Jupyter-Notebook-on-Raspberry-Pi/](https://www.instructables.com/Jupyter-Notebook-on-Raspberry-Pi/)

<pre>
sudo su -
apt-get update
apt-get install python3-matplotlib
apt-get install python3-scipy
pip3 install --upgrade pip
reboot
sudo pip3 install jupyter


</pre>


