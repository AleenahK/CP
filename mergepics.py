
"""
Using PIL library we are opening images and resizing them to their mean_height and mean_width 
because the video which will be created using cv2 library requires the input images of same 
height and width.

Resized images are included in an array and frame of video is set with the mean_height and 
mean_width. Then by looping, we are appending each image to that frame.

"""

# Importing libraries 
import os 
import cv2 
from PIL import Image 
import re

numbers = re.compile(r'(\d+)')

#To numerrically sort the files in order to correct file sequence
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

# Video Generating function 
image_folder = '/home/aleenahkahn/ASD/YOLOPreprocessedSSBD/ArmFlapping/crops/person/Arm flapping-hKf-IwHM6TI.mp4/' # make sure to use your folder 
video_name = 'armflapping_02.avi'
os.chdir('/home/aleenahkahn/ASD/Final_SSBD/ArmFlapping/') 
      
images = [img for img in os.listdir(image_folder) 
          if img.endswith(".jpg") or
             img.endswith(".jpeg") or
             img.endswith("png")] 
     
# Array images should only consider 
# the image files ignoring others if any 
#print(images)  
  
frame = cv2.imread(os.path.join(image_folder, images[0])) 
  
# setting the frame width, height width 
# the width, height of first image 
height, width, layers = frame.shape   
  
video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'MJPG'), 12, (width, height))  
  
# Appending the images to the video one by one 
for image in sorted(images, key=numericalSort):  
    video.write(cv2.imread(os.path.join(image_folder, image)))  
      
# Deallocating memories taken for window creation 
cv2.destroyAllWindows()  
video.release()  # releasing the video generated 
