import cv2
import sys
import os
import numpy as np

stimulus_name = sys.argv[1]
input_folder = "stimuli_pics"
output_folder = "objectness_salience"

#create stimulus-specific output folder if it does not exist
if not os.path.exists(os.path.join(output_folder,stimulus_name)):
    os.makedirs(os.path.join(output_folder,stimulus_name))

#get and sort input image data - see also VidToImg.py
name_images = os.listdir(os.path.join(input_folder,stimulus_name)) #get individuals images of video file
name_images.sort(key=lambda f: int(''.join(filter(str.isdigit, f)))) #sort alphanumerically
n_images = len(name_images)

# initialize OpenCV's objectness saliency
saliency = cv2.saliency.ObjectnessBING_create()
saliency.setTrainingPath("C:/Users/Nico/PowerFolders/project_video_salience/trained_models_BING/")

#### saliency model

#loop over images
i=0
while(i<2):
    image = cv2.imread(os.path.join(input_folder,stimulus_name,name_images[i])) #read image
    (success, saliencyMap) = saliency.computeSaliency(image) # compute the saliency map
    #saliencyMap = (saliencyMap * 255).astype("uint8") #changes 0-1 values to 255 grayscale

    # compute the bounding box predictions used to indicate saliency
    numDetections = saliencyMap.shape[0]

    # loop over the detections
    for i in range(0, min(numDetections, 5)):
    	# extract the bounding box coordinates
    	(startX, startY, endX, endY) = saliencyMap[i].flatten()

    	# randomly generate a color for the object and draw it on the image
    	output = image.copy()
    	color = np.random.randint(0, 255, size=(3,))
    	color = [int(c) for c in color]
    	cv2.rectangle(output, (startX, startY), (endX, endY), color, 2)
    	# show the output image
    	cv2.imshow("Image", output)
    	cv2.waitKey(0)

    #write to file
    #cv2.imwrite(os.path.join(output_folder,stimulus_name,stimulus_name+"_salience"+str(i)+".jpg"), saliencyMap) #write salience map
    #print(os.path.join(output_folder,stimulus_name,stimulus_name+"_salience"+str(i)+".jpg")) #print processed salience map
    i+=1

cv2.destroyAllWindows()
