## [../](../)

#  Raspberry Pi System Installation

Get a SD card with 8 GB or more storage and a SD card USB reader

Download and install, then use the Raspberry Pi Imager:

[https://www.raspberrypi.org/software/](https://www.raspberrypi.org/software/)

Turn on the pi click through all the things, put it on the wifi network.

## Install Apache and PHP so that geometron can run:

```
sudo apt update
sudo apt install apache2 -y
sudo apt install php libapache2-mod-php -y
```

## Install geometron with this document for self-documentation and replication

```
cd /var/www/html
sudo rm index.html
sudo curl -o replicator.php https://raw.githubusercontent.com/LafeLabs/pi/main/php/replicator.txt
cd ..
sudo chmod -R 0777 *
cd html
php replicator.php
sudo chmod -R 0777 *
```

Check the IP address by hovering over the wifi icon, put that into the browser on another machine on the same local wifi network to see and edit the server.  Or open a browser on the pi and point it to [http://localhost](http://localhost)

## Enable VNC

From the menu, select

preferences>raspberry pi configuration>interfaces

click radio button to turn VNC on

## Set up to have names for other servers

edit hosts file to have the IP address of the other servers and then the name you want to use, copying the format in the existing file.

```
sudo nano /etc/hosts
```

edit, and use control-x and say "yes" to save changes.

## Install arduino

```
sudo apt-get install arduino
```

this installs a old version which is missing some features, namely the serial plotter.  following more complicated instructions leads to non-working version which is impossible to uninstall.


how to do the tar ball thing to get a later version of arduino which has the plotting

[https://www.raspberrypi-spy.co.uk/2020/12/install-arduino-ide-on-raspberry-pi/](https://www.raspberrypi-spy.co.uk/2020/12/install-arduino-ide-on-raspberry-pi/)


## Add python that we need

matplotlib
```
sudo apt install python3-matplotlib
```

[https://matplotlib.org/](https://matplotlib.org/)

matplotlib install:

```
sudo apt install python3-matplotlib
```

[https://matplotlib.org/](https://matplotlib.org/)

[https://www.instructables.com/Jupyter-Notebook-on-Raspberry-Pi/](https://www.instructables.com/Jupyter-Notebook-on-Raspberry-Pi/)

```
sudo su -
apt-get update
apt-get install python3-matplotlib
apt-get install python3-scipy
pip3 install --upgrade pip
reboot
sudo pip3 install jupyter
```

