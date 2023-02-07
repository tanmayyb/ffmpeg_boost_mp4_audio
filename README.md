# Python Script to Boost MP4 audio using ffmpeg
### Project Time: 
1.5 hours
### Objective:
To automate the audio boosting of my prof's low-volume video lectures. </br>
### Result:
The script can boost audio of files that follow this directory structure:
```
├── Week1
│   └── Week1Lec1.mp4
├── Week2
│   ├── W2Lec1.mp4
│   └── W2Lec2.mp4
└── boost_audio.py
```
Basically put all our video files in their respective weeks and then run the script in the main folder.
It will boost the audio in the files and then place them in an auto-created `boosted` folder for each week.
```
├── Week1
│   ├── Week1Lec1.mp4
│   └── Boosted
│       └──  Week1Lec1.mp4
├── Week2
│   ├── W2Lec1.mp4
│   ├── W2Lec2.mp4
│   └── Boosted
│       └──  W2Lec1.mp4
│       └──  W2Lec2.mp4
└── boost_audio.py
```

### Notes
- The file names should not have any spaces in them. The program will not be able to find the files.
- Please have FFMPEG and Python3 installed in your system. FFMPEG should be added to path if you're on windows.
