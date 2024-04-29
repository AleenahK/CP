
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
image_folder = '/home/aleenahkahn/ASD/YOLOPreprocessedSSBD/Spinning/crops/person/' # make sure to use your folder 
output_dir = '/home/aleenahkahn/ASD/Final_SSBD/Spinning/'
c = 0
for path, folders, files in os.walk(image_folder):
	for folder_name in folders:
	   c = c + 1
	   video_name = 'spinning_'+str(c)+'.avi' 
	   images = [img for img in os.listdir(os.path.join(path, folder_name)) 
     	             if img.endswith(".jpg") or
     	                img.endswith(".jpeg") or
     	                img.endswith("png")] 
     
# Array images should only consider 
# the image files ignoring others if any 
#print(images)  
  
	   #frame = cv2.imread(os.path.join(os.path.join(path, folder_name), images[0])) 
  
# setting the frame width, height width 
# the width, height of first image 
	   #height, width, layers = frame.shape   
  
	   video = cv2.VideoWriter(os.path.join(output_dir, video_name), cv2.VideoWriter_fourcc(*'MJPG'), 12, (224, 224))  
  
# Appending the images to the video one by one 
	   for image in sorted(images, key=numericalSort):  
         	   video.write(cv2.imread(os.path.join(os.path.join(path, folder_name), image)))  
      
# Deallocating memories taken for window creation 
cv2.destroyAllWindows()  
video.release()  # releasing the video generated 
