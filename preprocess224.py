
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

# Video Generating function 
def generate_video(image_folder, folder_name): 
	#image_folder = os.listdir(f"{path}/{folder_name}") # make sure to use your folder 
	video_name = 'armflapping01.avi'
	#os.chdir("/home/aleenahkahn/ASD/PreprocessedSSBD/ArmFlapping/crops/") 
	
	images = [img for img in os.listdir(image_folder) 
			if img.endswith(".jpg") or
				img.endswith(".jpeg") or
				img.endswith("png")] 

	frame = cv2.imread(os.path.join(image_folder, images[0])) 

	# setting the frame width, height width 
	# the width, height of first image 
	height, width, layers = frame.shape
	os.chdir('/home/aleenahkahn/ASD/PreprocessedSSBD/ArmFlapping/final/') 

	video = cv2.VideoWriter(video_name, 0, 1, (width, height)) 

	# Appending the images to the video one by one 
	for image in images: 
		video.write(cv2.imread(os.path.join(image_folder, image))) 
	
	# Deallocating memories taken for window creation 
	cv2.destroyAllWindows() 
	video.release() # releasing the video generated 


# Checking the current directory path 
print(os.getcwd()) 
directory = '/home/aleenahkahn/ASD/YOLOPreprocessedESBD/ArmFlapping/crops/person/'
for path, folders, files in os.walk(directory):
	for folder_name in folders:
     	   print(f"Processing Folder : {folder_name}")
     	   new_height = 224
     	   new_width = 224
     	   num_of_images = len(os.listdir(f"{path}/{folder_name}")) 
     	   print(num_of_images) 
     	   #for file in os.listdir(f"{path}/{folder_name}"): 
	   #add os.path.join(folder_name
     	      #im = Image.open(os.path.join(os.path.join(path, folder_name) , file)) 
     	      #print(im)
     	      #width, height = im.size 
     	      #mean_width += width 
     	      #mean_height += height 
	      # im.show() # uncomment this for displaying the image 
	      
	      # Finding the mean height and width of all images. 
	      # This is required because the video frame needs 
	      # to be set with same width and height. Otherwise 
	      # images not equal to that width height will not get 
	      # embedded into the video 
     	   #mean_width = int(mean_width / num_of_images)
     	   #mean_height = int(mean_height / num_of_images) 
     	   #print("============================================")
     	   #print(mean_height) 
     	   #print(mean_width)
     	   #print("============================================")
	   
	   # Resizing of the images to give 
	   # them same width and height 
     	   for file in os.listdir(f"{path}/{folder_name}"): 
     	      if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"): 
	         # opening image using PIL Image 
                 im = Image.open(os.path.join(os.path.join(path, folder_name) , file)) 
		 
	         # im.size includes the height and width of image 
                 width, height = im.size 
                 print(width, height) 
	
                 # resizing 
                 imResize = im.resize((new_width, new_height), Image.LANCZOS) 
                 save_path = os.path.join(os.path.join(path, folder_name), file)
                 imResize.save( save_path, 'JPEG', quality = 95) # setting quality
                 nwidth, nheight = imResize.size
                 print(nwidth, nheight)
                 # printing each resized image name 
                 print(im.filename.split('\\')[-1], " is resized") 
	
	   # Calling the generate_video function
     	      #generate_video(os.path.join(path, folder_name), folder_name) 
     	   #generate_video(os.path.join(path, folder_name), folder_name)
