import cv2
import sys
import os

vid_name = sys.argv[1]
vid_path = sys.argv[2]
#vid_name = "coralreef"
#vid_path = "C:/Users/Nico/PowerFolders/Paper_AIMS-LEAP_ETcore/stimuli/nonhuman"

#get the path of the vid_name in vid_path (search for the video)
for path in os.listdir(vid_path):
    if vid_name in path:
        full_path = os.path.join(vid_path, path)


output_folder = "stimuli_pics"
if not os.path.exists(output_folder):
    os.mkdir(output_folder)
os.chdir(output_folder)

#create folder for pics if not existing
if not os.path.exists(vid_name):
    os.mkdir(vid_name)
os.chdir(vid_name)

#loop to create pics from vid
cap = cv2.VideoCapture(full_path)
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite(vid_name+str(i)+'.jpg',frame)
    print(vid_name+str(i)+'.jpg')
    i+=1

cap.release()
cv2.destroyAllWindows()
