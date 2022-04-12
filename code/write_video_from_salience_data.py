import cv2
import numpy as np
import glob
import os

#get paths of files and sort alphanumerically
#img_array = os.listdir('C:/Users/Nico/PowerFolders/project_video_salience/stimuli_salience/artist/') #get individuals images of video file
#file_list = glob.glob('C:/Users/Nico/PowerFolders/project_video_salience/stimuli_salience/artist/*.jpg')
file_list = glob.glob('C:/Users/Nico/PowerFolders/project_video_salience/motion_salience/Pingu_doctors/Pingu_doctors_scene0/*.jpg')
file_list.sort(key=lambda f: int(''.join(filter(str.isdigit, f)))) #sort alphanumerically

img_array = []

#for filename in glob.glob('C:/Users/Nico/PowerFolders/project_video_salience/stimuli_salience/artist/*.jpg'):
for filename in file_list:
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
    print(filename)

codec = cv2.VideoWriter_fourcc('D','I','V','X') #in this case divx
framerate = 24
#out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), framerate, size)
out = cv2.VideoWriter('motion_salience_video_pingudoctors_scene0.avi',codec, framerate, size)
# --> output as mpeg file

for i in range(len(img_array)):
    out.write(img_array[i])
    print(str(img_array[i]))
out.release()
