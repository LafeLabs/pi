#  Raspberry Pi

 - [http://localhost](http://localhost)
 - [../](../)
 - [codeserver/](codeserver/)
 - [fork.html](fork.html)
 - [editor.php](editor.php)
 - [readme.html](readme.html)
 - [home](index.html)
 - [scrolleditor.html](scrolleditor.html)
 - [set.html](set.html)
 - [dnagenerator.php](dnagenerator.php)
 - [global replicator code link](https://raw.githubusercontent.com/LafeLabs/pi/main/php/replicator.txt)
 - [local replicator code link](php/replicator.txt)
 - [replicator.php](replicator.php)

## install

Get a SD card with 8 GB or more storage and a SD card USB reader

Download and install, then use the Raspberry Pi Imager:

[https://www.raspberrypi.org/software/](https://www.raspberrypi.org/software/)

Turn on the pi click through all the things, put it on the wifi network.

## Install Apache and PHP so that geometron can run:

<pre>
sudo apt update
sudo apt install apache2 -y
sudo apt install php libapache2-mod-php -y
</pre>

## Install geometron with this document for self-documentation and replication

<pre style = "overflow:scroll">
cd /var/www/html
sudo rm index.html
sudo curl -o replicator.php https://raw.githubusercontent.com/LafeLabs/pi/main/php/replicator.txt
cd ..
sudo chmod -R 0777 *
cd html
php replicator.php
sudo chmod -R 0777 *
</pre>

Check the IP address by hovering over the wifi icon, put that into the browser on another machine on the same local wifi network to see and edit the server.  Or open a browser on the pi and point it to [http://localhost](http://localhost)

## Enable VNC

From the menu, select

preferences>raspberry pi configuration>interfaces

click radio button to turn VNC on

## Set up to have names for other servers

edit hosts file to have the IP address of the other servers and then the name you want to use, copying the format in the existing file.

<pre>
sudo nano /etc/hosts
</pre>
edit, and use control-x and say "yes" to save changes.

## Install arduino

<pre>
sudo apt-get install arduino
</pre>

following more complicated instructions leads to non-working version which is impossible to uninstall.

## Add python that we need

matplotlib
<pre>
sudo apt install python3-matplotlib
</pre>

[https://matplotlib.org/](https://matplotlib.org/)



## Roles of the Raspberry pi:

 - teaching tool
 - radio
 - video chat node
 - remote sensor
 - remote off grid social media
 - network machine for building free wifi networks
 - web server
 - web client
 - host for organic media: geometron, bioweb, chaos, etc
 - ipython notebooks to analyze data and share science
 - program arduino

Roles for the Arduino:

 - control neopixel array around the unit
 - control motors, both DC and AC
 - control high intensity lights, signal lights
 - record sensor data

Elements of a station:

 - lead acid battery
 - battery charger
 - solar panel
 - cart with bike wheels
 - rugged rain and snow and wind proof enclosure
 - protected screen
 - rugged keyboard, with cover
 - rugged mouse with cover
 - neopixel array
 - beacon light
 - raspberry pi
 - stand
 - fold up chair and fold out desk
 - projector
 - hydroelectric turbine
 - bike generator pickup, which can integrate with a hydroelectric bike drive, using the bike wheels on the cart
 - water sensor array on arduino
 - arduino shield which controls an arbitrary motor: AC, DC, wall power 
 - picam
 - optical microscope for viewing water
 - speakers
 - microphone
 - software defined radio receiver 
 - generic trash robot and controller
 - power train for bike wheels for cart makes it into a fully mobile robot, which can be driven by arduino with controller

Skills for an operator

 - set up a new raspberry pi(software)
 - get apache, PHP and geometron installed
 - control the pi remotely using VNC
 - build the enclosure, cart, tower
 - learn to program arduino with blink
 - learn to plot sensor data in arduino IDE
 - learn to control neopixels
 - plot data from arduino in jupyter notebooks, share notebooks
 - replicate geometron from pi to private machine to github and back to pi
 - run video chat over pi using VNC 
 - GNU radio, learn to tune into radio stations, find a transmitter
 - build a hydroelectric generator
 - set up a solar power plant with a car battery

Sensors:

 - water level
 - water current
 - water temperature
 - ice movement
 - water salinity
 - specific contaminant measurements, oil, phosphate, etc
 - microscope watching the water on webcam
 - wind

Applications

 - job board, personals, for sale, mutual aid
 - zines, art sharing
 - plant and animal lore distribution locally to a place
 - local wildlife and nature news
 - water monitoring 
 - remote control of machines
 - remote control of signal lights
 - video chat with passerby from around the world
 - fishery monitor with underwater cameras
 - platform for environmental science
 - applied physics teaching platform
 - video game system, entertainment
 

Really nice project to do video calls on pi:

https://www.hackster.io/rundhall/raspberry-pi-based-video-call-for-seniors-00dcc2



Wireless networking free and open resource:

[https://commotionwireless.net/](https://commotionwireless.net/)

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

extender?

"range extender" = repeater

https://www.techwalla.com/articles/wireless-bridge-vs-repeater


[https://pimylifeup.com/raspberry-pi-wifi-extender/](https://pimylifeup.com/raspberry-pi-wifi-extender/)

how to edit hosts file to give raspberry pi a name:

[https://www.howtogeek.com/howto/27350/beginner-geek-how-to-edit-your-hosts-file/](https://www.howtogeek.com/howto/27350/beginner-geek-how-to-edit-your-hosts-file/)

This is problematic with random clients but works if you can set up each device.

To replicate this system, create a new github repository, get PHP working from the command line on your machine(mac, pc, linux all work), then copy the file [php/replicator.txt](php/replicator.txt) into a new file called replicator.php, and run it.  

<pre>
php replicator.php
</pre>


Once you've run it, be sure permissions are ok, and run 

<pre>
php -S localhost:80
</pre>

from the command line, then point a browser on your machine to "[http://localhost](http://localhost)".  Then click on the [editor](editor.php) to edit the code.  Use the editor to change the value of the code in php/replicator.txt to point to the dna.txt and replicator.txt raw text files of your new repository, then run the program [text2php.php](text2php.php) to convert the text you edited to a live php script.  To add files, instead of pointing your browser to editor.php, point it to editor.php?newfile=[name of new file].  When you've added any files, run [dnagenerator.php](dnagenerator.php) to add them to your dna.  Then update the global copy of your repository on Github, and you should be able to copy your newly modified replicator code into the root web directory *anywhere* that has a running web server, run it from any browser, and your web app will replicate.  

That new instance can then be modified in the same way, the code updated in the replicator to point to the new global instance as it evolves.  Any given app can replicate an arbitrary number of times as is, or can mutate instantly and be abandoned.  It's up to you. 

Web servers on which this have been tested include paid hosts dreamhost and bluehost, free hosting at 000webhost, php localhosts on windows, mac and linux, Apache run on a Raspberry Pi and on an Ubuntu virtual machine, on windows and linux machines with [XAMPP](https://www.apachefriends.org/index.html), on the Android using [KSWEB](https://www.kslabs.ru/), on iOS using [phpwin](https://app.phpwin.org/).  You need write permission and PHP running and you're good to go.  

To install Apache, PHP and Geometron from the command line on Raspberry Pi, 

enter:

<pre>
sudo apt update
sudo apt install apache2 -y
sudo apt install php libapache2-mod-php -y
</pre>

then

<pre style = "overflow:scroll">
cd /var/www/html
sudo rm index.html
sudo curl -o replicator.php https://raw.githubusercontent.com/LafeLabs/bioweb/main/php/replicator.txt
cd ..
sudo chmod -R 0777 *
cd html
php replicator.php
sudo chmod -R 0777 *
</pre>

### Use cases

 - [geometron](https://www.trashrobot.org/)
 - shopping center pages
 - corner market
 - rideshare
 - mutual aid coordination 
 - personals ads
 - local news feeds
 - dumpster updates for scavengers
 - self-replicating open source hardware replicators
 - self-replicating custom calculators for specific technical applications
 - building general self-replicating HTML applications to do any arbitrary task
 - personal home pages
 - local bulletin boards in a community space served over the wifi
 - self-replicating zines


## Structural Elements of the System:

Languages: PHP, HTML, JavaScript, CSS, Markdown, JSON

THERE ARE NO DATABASES

 - [replicator.php](php/replicator.txt): replicates the system using the file [data/dna.txt](data/dna.txt)
 - [fileloader.php](php/fileloader.txt): loads and prints files from the server filesystem 
 - [filesaver.php](php/filesaver.txt): saves files to the server filesystem
 - [editor.php](php/editor.txt): a general code editor which can edit all parts of the system, and formats code using the [Ace.js library](https://ace.c9.io/)
 - [text2php.php](php/text2php.txt): a script which copies every file in the php directory(all of which use the .txt extension so browsers can read them) into the main directory with the .php extension so that they can run.  This prevents editor.php from breaking things in real time while they are edited.
 - [dnagenerator.php](php/dnagenerator.txt): this script reads from the server file system to see what files exist and put them in the file [data/dna.txt](data/dna.txt) so that the replicator can find them all using the dna
 - [setreplicator.php](php/setreplicator.txt): copies a set of files described by the JSON file [data/set.txt](data/set.txt)
 - [removephp.php](php/removephp.txt): removes all .php scripts, making the page passive.  This will break fileloader.php which breaks index.html, so it can also be used with the "keeploader" flag with fileloader.php?keeploader to keep the loader and delete all other .php scripts to avoid a page getting edited if it faces the wider Internet and you don't want it "hacked"
 - [setreplicator.php](php/setreplicator.txt): a script which copies all the files listed in [data/set.txt](data/set.txt)
 - [mkdir.php](php/mkdir.txt): makes a new directory using mkdir
 - [dir.php](php/dir.txt): list contents of a directory
 - [rdelete.php](php/rdelete.txt): recursively delete everything in a directory or any given thing.  This totally destroys all contents of something instantly with no undo
 - [README.md](README.md): this document. By default index.html and readme.html both read this, and it is also by default the document seen on the github repository
 - [readme.html](readme.html): a page which reads the README and converts it to html for easy viewing in a browser
 - [index.html](index.html): home page, where browsers start pointing to.  Edit to anything using editor.php.  There are no limits to what this can do.
 - [scrolleditor.html](scrolleditor.html): the editor for markdown files, in this case just README.md but if you replicate a more full version of Geometron it can edit an arbitrary number of markdown files, and it is easily edited using editor.php to edit other types of file of all kinds
 - [set.html](set.html):  The operation page for the self-replicating set of files found in [data/set.txt](data/set.txt) which points to source and destination locations
 - [fork.html](fork.html): lists directories with links to all of them, allows for creating new directories and also deleting any directory
 - [data/dna.txt](data/dna.txt): a JSON file which lists all the files replicated by replicator.php
 - [data/set.txt](data/set.txt): a JSON file which lists files to replicate using setreplicator.php



