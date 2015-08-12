import os
import sys
import time
print("Checking for Pygame Installation...")
pyg = None
done = 0
try:
  import pygame #Tries to import pygame
  print("You have pygame installed. I will now download the PiMusic files.")
  print("Downloading PiMusic Files...")
  time.sleep(2)
  os.system("git clone https://github.com/InsightGit/PiMusic.git")
  print("Done Installing PiMusic! Start it by typing in cd PiMusic and python3 PiMusic.py")
  sys.exit
except ImportError:
        print("You do not have pygame installed. I will install it for you.")
        while done != 1:
                try:
                        while pyg != "y" or pyg != "n":
                                 pyg = input("This will take about 30-60 mins. Is that okay?")
                                 if pyg == "y":
                                        ("Installing Dependencies...")
                                        time.sleep(2)
                                        os.system("sudo apt-get update")
                                        os.system("sudo apt-get install mercurial")
                                        os.system("sudo apt-get install libsdl-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev -y")
                                        os.system("sudo apt-get install libsmpeg-dev libportmidi-dev libavformat-dev libswscale-dev -y")
                                        os.system("sudo apt-get install python3-dev python3-numpy -y")
                                        print("Downloading PyGame Files...")
                                        time.sleep(2)
                                        os.system("hg clone https://bitbucket.org/pygame/pygame")
                                        os.system("cd pygame")
                                        print("Building PyGame...")
                                        time.sleep(2)
                                        os.system("python3 setup.py build")
                                        print("Installing PyGame...")
                                        time.sleep(2)
                                        os.system("sudo python3 setup.py install")
                                        print("Downloading PiMusic Files...")
                                        time.sleep(2)
                                        os.system("git clone https://github.com/InsightGit/PiMusic.git")
                                        print("Done Installing PiMusic! Start it by typing in cd PiMusic and python3 PiMusic.py")
                                        sys.exit
                                        if pyg == "n":
                                                print("Aborting")
                                                sys.exit()
                except KeyboardInterrupt:
                        None
