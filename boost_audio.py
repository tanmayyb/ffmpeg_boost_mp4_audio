volume_boost_level = 5.5

import os, json
import subprocess
from time import time
start_time = time()

print("launched at: ", os.getcwd(), "\n\n")

# list in main dir
print(os.listdir())
dir = 'Week1'
print(os.path.isdir(dir))

# interate through all the directories
for dirname in os.listdir():
    if os.path.isdir(dirname):
        dir = dirname
        dirtime = time()

        # list in second dir
        print("current directory:\t\t", dir)
        print("files inside this directory:\n", os.listdir(dir))

        # check if boosted folder exists
        if not os.path.isdir(dir+"/boosted"):
            print("no audio encoded files in this dir, creating folder...")
            os.makedirs(dir+"/boosted")

        # encode files in a particular week
        for filename in os.listdir(dir):
            if (filename.endswith(".mp4")): #or .avi, .mpeg, whatever.
                print("encoding file: ", filename, " with ffmpeg...")
                file_encoding_time = time()

                command = "ffmpeg -i "+ dir + "/" + filename+ " -filter:a volume=" + str(volume_boost_level)+ " " + dir + "/boosted/" + filename+""
                print("ffmpeg command:\n"+command+"\n\n")        
                subprocess.call(command, shell=True)

                print("\njust created:\t\t"+dir+"/boosted/"+filename+" -Boosted")
                print("using command:\n"+command)
                print("encoding time for file:\t\t", str(time()-file_encoding_time), "s" )
            else:
                continue
        print("time spent in directory:\t\t"+str(time()-dirtime),"s\n\n\n" )
    
"""
#ffmpeg -i 'Week1/Week2_Part_03_Inductance - Electric Circuits.mp4' -filter:a "volume=5.0" 'Week1/boosted/Week2_Part_03_Inductance - Electric Circuits - Boosted.mp4'
"""
