# PiMusic
A very lightweight and simple music player for the Raspberry Pi.

Supports Uncompressed WAV, MP3, OGG, XM and MOD.

Requires Pygame

To Run:

$ cd PiMusic

$ python3 PiMusic.py

To install:
type wget https://www.dropbox.com/s/ecr95apk8sw5y21/autoinstall.py?dl=1 and python3 autoinstall.py

Then follow the on-screen instructions

Manual install:

if pygame is installed:

$ git clone https://github.com/InsightGit/PiMusic.git

if pygame is not installed:

$ sudo apt-get install mercurial

$ hg clone https://bitbucket.org/pygame/pygame

$ cd pygame

$ sudo apt-get install libsdl-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev

$ sudo apt-get install libsmpeg-dev libportmidi-dev libavformat-dev libswscale-dev

$ sudo apt-get install python3-dev python3-numpy

$ python3 setup.py build

$ sudo python3 setup.py install

$ git clone https://github.com/InsightGit/PiMusic.git





