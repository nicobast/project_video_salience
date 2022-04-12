import cv2
import sys
import os

stimulus_name = sys.argv[1]
input_folder = "stimuli_pics"
output_folder = "stimuli_salience"

#create stimulus-specific output folder if it does not exist
if not os.path.exists(os.path.join(output_folder,stimulus_name)):
    os.mkdir(os.path.join(output_folder,stimulus_name))

#get and sort input image data - see also VidToImg.py
name_images = os.listdir(os.path.join(input_folder,stimulus_name)) #get individuals images of video file
name_images.sort(key=lambda f: int(''.join(filter(str.isdigit, f)))) #sort alphanumerically
n_images = len(name_images)

# initialize OpenCV's static saliency spectral residual detector and
saliency = cv2.saliency.StaticSaliencySpectralResidual_create()

#### saliency model after
# Hou, X., & Zhang, L. (2007, June). Saliency detection: A spectral residual approach. In 2007 IEEE Conference on computer vision and pattern recognition (pp. 1-8). Ieee.

#loop over images
i=0
while(i<n_images):
    image = cv2.imread(os.path.join(input_folder,stimulus_name,name_images[i])) #read image
    (success, saliencyMap) = saliency.computeSaliency(image) # compute the saliency map
    saliencyMap = (saliencyMap * 255).astype("uint8") #changes 0-1 values to 255 grayscale
    cv2.imwrite(os.path.join(output_folder,stimulus_name,stimulus_name+"_salience"+str(i)+".jpg"), saliencyMap) #write salience map
    print(os.path.join(output_folder,stimulus_name,stimulus_name+"_salience"+str(i)+".jpg")) #print processed salience map

    #show image
    #cv2.imshow("Image", image)
    #cv2.imshow("Salience", saliencyMap)
    #cv2.waitKey(20)

    i+=1
