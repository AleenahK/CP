#!/usr/bin/env python
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import *

# Replace the filename below.
in_directory = "/home/aleenahkahn/ASD/Final_SSBD/Spinning/"
out_directory = "/home/aleenahkahn/ASD/SSBD_clips/Spinning/"
file_name = "spinning_20.avi"
input_file = VideoFileClip(os.path.join(in_directory, file_name))
duration = input_file.duration
counter = int(duration/10)
starttime = 1
endtime = 10
for i in range(1,counter+1):
  out_file_name = os.path.splitext(file_name)[0]+"_"+str(i)+".avi"
  ffmpeg_extract_subclip(os.path.join(in_directory, file_name), starttime, endtime, targetname=os.path.join(out_directory, out_file_name))
  starttime = starttime + 10
  endtime = endtime + 10
  
  
#with open("times.txt") as f:
  #times = f.readlines()
#times = [x.strip() for x in times] 

#if (t < clip_size):
    #print("10 is less than 15")

#for time in times:
  #starttime = int(time.split("-")[0])
  #endtime = int(time.split("-")[1])
  #ffmpeg_extract_subclip(required_video_file, starttime, endtime, targetname=str(times.index(time)+1)+".mp4")
