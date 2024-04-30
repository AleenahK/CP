## CAP 5516 - Course Project

# Step 01:
Download the SSBD and ESBD datasets from the following links:

SSBD:
https://drive.google.com/file/d/1tQ89MXK4TXYTXPV8Gtk86I_tNM8VrCXU/view?usp=sharing

ESBD:
link for the ESBD dataset is shared in the project report document as it is still not made publicly available.


# Stape 02:
Since the two datasets contain a large portion of the background or other subjects, 
we first preprocess the videos to obtain cleaner data that include target children 
showing autistic behaviors. We use the popular YOLOv5 to perform object detection 
[ref]which is pretrained on the COCO [ref] dataset. To extract only the child from
the video frame we use the class 0 which is the "person" class.

Use the following commands to set up the environment and to perform inference to 
get target child frames from the pretrained YOLOv5 using the yolovgs.pt weights:

Clone the YOLOv5 Github repository:
$ git clone https://github.com/ultralytics/yolov5

Change directory to yolov5:
cd yolov5

Create conda environment with python 3.8:
conda create --name yolov5-env python=3.8

Activate conda environment:
conda activate yolov5-env

Install required packages using requirements.txt file:
pip install -r requirements.txt

Perform inference by executing the detect.py script: 
--classes 0 refers to the "Person" class.
--save-crop helps in getting the cropped frames saved as individual files. 
python detect.py --weights yolov5s.pt --classes 0 --save-crop --source '/home/aleenahkahn/ASD/SSBD dataset/

With the help of YOLOv5, we obtain the cropped frames of the target children which
will help in more accurate ASB behavior recognition results.
 
# Step 03:
The cropped frames obtained from YOLOv5 are individual cropped frames with different heights and widths. 
We write a simple python script called preprocess.py to convert the target cropped images to video files
using mean height and width with the help of PIL and OpenCV libraries.

python3 preprocess.py (converts to mean height and width)
or
python3 preprocess224.py (converts to 224x224)

Now we will merge the individual images to create the videos again:
python3 mergepics.py
make sure to use the provided numericalSort function to merge the files in the correct sequence.

Next, we will split the above pre-processed videos into small clips of equal size.
conda activate create-video

pip install moviepy
python3 create_subclips.py

Finally, we split the clips into train, val and test sets with ratio 75%, 15% and 10% respectively and 
create the zipped file. 
To create a tar.gz file:
tar -czvf SSBD.tar.gz /home/aleenahkahn/ASD/data/SSBD
or
tar -czvf ESBD.tar.gz /home/aleenahkahn/ASD/data/ESBD

# Step 04:
The rest of the steps for training and evaluation of the model are defined in the provided notebooks. 
