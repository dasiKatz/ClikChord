import wave
import math

#קוד זה מחלק את השיר לשניות לפי מה שאני מבקשת ממנו
def chordSStack(filename, time):
    read = wave.open(filename, 'r')

#get sample rate
    frameRate = read.getframerate()

#get number of frames
    numFrames = read.getnframes()

#get duration
    duration = numFrames/frameRate

#get all frames as a string of bytes
    frames = read.readframes(numFrames)

#get 1 frame as a string of bytes
    oneFrame = read.readframes(1)

#framerate*time == numframesneeded
    numFramesNeeded=frameRate*time

#numFramesNeeded*oneFrame=numBytes
    numBytes = numFramesNeeded*oneFrame

#splice frames to get a list strings each representing a 'time' length
#wav file
    x=0
    wavList=[]
    while x+time<=duration:
        curFrame= frames[x:x+time]
        x=x+time
        wavList.append(curFrame)
        print(x)
chordSStack( "final.wav",2)
