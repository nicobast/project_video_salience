import cv2 #required?
import sys
import os
import numpy as np #diff
#import ffmpeg #to cut videos
#import csv

#standard values
vid_name = sys.argv[1]
input_folder = "C:/Users/Nico/PowerFolders/project_video_salience/stimuli_pics/"
output_folder = "stimuli_scene"

#get the path of the vid_name in input_folder (search for the video)
for path in os.listdir(input_folder):
    if vid_name in path:
        full_path = os.path.join(input_folder, path)

#input files
input_images = os.listdir(full_path) #get individuals images of video file
input_images.sort(key=lambda f: int(''.join(filter(str.isdigit, f)))) #sort alphanumerically

##set frame rate based on video information
if vid_name in ['artist','musicbooth','dollhouse']:
    # note if(vid_name %in% c('artist','musicbooth','dollhouse')){fps<-24}
    fixed_framerate=24
else:
    fixed_framerate=25

#create out folder for scenes if not existing
if not os.path.exists(output_folder):
    os.mkdir(output_folder)
os.chdir(output_folder)

#create folder for specific scene if not existing
if not os.path.exists(vid_name):
    os.mkdir(vid_name)
os.chdir(vid_name)

##set scenes per video - see video_stimuli_scenes.csv
if vid_name == 'musicbooth':
    scenes_frame_start = [0,119]
if vid_name == 'dollhouse':
    scenes_frame_start = [0,283,914,979,1131,1186,1568,1731,1923,2103,2182,2269,2372,2528,2587,2654,2729,2811,2864]
if vid_name == 'artist':
    scenes_frame_start = [0,100,192,243,326,448,514,586,650,788,842,914,981,1020,1087,1118,1296,1368,1428,1533,1710,1784,1845,2114,2145,2193,2241,2280]
if vid_name == '50faces':
    scenes_frame_start = [0,47,84,115,187,262,348,440,494,577,632,680,819,874,953]
if vid_name == 'coralreef':
    scenes_frame_start = [0,70,140,180,227,283]
if vid_name == 'birds':
    scenes_frame_start = [0]
if vid_name == 'flowersstars':
    scenes_frame_start = [0]
if vid_name == 'Pingu1':
    scenes_frame_start = [0,284,398,464,549,570,615,871,900]
if vid_name == 'Pingu_doctors':
    scenes_frame_start = [0,256,294,386,475,584,611,679,732,1012,1109,1147,1229,1289,1398,1474,1563,1603]

#define length of each scene
scenes_len = scenes_frame_start + [len(input_images)] #length of scenes on frames
scenes_len = np.diff(scenes_len) #length of scenes on frames
scenes_len = scenes_len.tolist() #add length of last scene - not encoded in file

print(len(input_images))
print(sum(scenes_len))

# ffmpeg approach
# input_images = ffmpeg.input(path_input_images[scenes_frame_start[0]:scenes_frame_start[1]], pattern_type='glob', framerate=fixed_framerate)
# stream = ffmpeg.output(input_images, 'dummy.mp4')
# stream.run()

# Determine the width and height from the first image
frame = cv2.imread(os.path.join(full_path,input_images[0]))
height, width, channels = frame.shape

# #LOOPS
#loop of scenes
for i in range(len(scenes_frame_start)):
    print(str(i))

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case
    scene_output_file = (vid_name+"_scene"+str(i)+'.mp4v')
    out = cv2.VideoWriter(scene_output_file, fourcc, fixed_framerate, (width, height))

    #loop of images within scene
    for image in input_images[scenes_frame_start[i]:(scenes_frame_start[i]+scenes_len[i])]:
        print(image)

        image_path = os.path.join(full_path, image)
        frame = cv2.imread(image_path)

        out.write(frame) # Write out frame to video

    out.release() #save object to file
    cv2.destroyAllWindows()
