# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments - so a path to image is provided on calling the function
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

# load the input image
image = cv2.imread(args["image"])

# initialize OpenCV's static saliency spectral residual detector and
# compute the saliency map
saliency = cv2.saliency.StaticSaliencySpectralResidual_create()
(success, saliencyMap) = saliency.computeSaliency(image)

saliencyMap = (saliencyMap * 255).astype("uint8") #changes 0-1 values to 255 grayscale

# show map
#cv2.imshow("Image", image)
#cv2.imshow("Output", saliencyMap)

cv2.imwrite("stimuli_salience/test_salience.jpg", saliencyMap)
cv2.waitKey(0)
