import cv2
import sys
import os

###NOTE: takes videos split to scenes as input - as videos with different scenes will cause the motion alorithm to provide false positives

video_folder = "stimuli_scene"

input_folder = sys.argv[1]
output_folder = "motion_salience"

scenes = os.listdir(os.path.join(video_folder,input_folder))
scenes.sort(key=lambda f: int(''.join(filter(str.isdigit, f)))) #sort alphanumerically

for scene in scenes:

    #input_folder = sys.argv[1]
    # for loop stimulus name
    stimulus_file = scene
    stimulus_name = os.path.splitext(scene)[0]

    #create stimulus-specific output folder if it does not exist
    output_path = os.path.join(output_folder,input_folder,stimulus_name)
    if not os.path.exists(output_path):
       os.makedirs(output_path)

    #open video of the scene (ceated by split_images_to_scenes)
    video_path = os.path.join(video_folder,input_folder,stimulus_file)
    cap = cv2.VideoCapture(video_path)

    # amount_of_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    # print(amount_of_frames)

    #---> identify MOTION SALIENCE
    # loop over frames from the video file stream
    i=1
    while (cap.isOpened()):

        # grab the frame from the video
        # cap.set(1,i) #set frame of the video stream
        boolr, frame = cap.read() #read the frame of the stream
        if boolr == False: #break if cannot be read
            break
        print(i)

        #if saliency does not exist create it
        try:
            saliency
        except:
            #saliency = cv2.createBackgroundSubtractorMOG2(history = 25, detectShadows = False)
            saliency = cv2.createBackgroundSubtractorMOG2(history = 500, varThreshold = 30, detectShadows = False)

            #default varThresholdGen = 9
            #default varThreshold = 16
            #default history = 500 <- shorter adaption

        ## convert the input frame to grayscale and compute the saliency
        ## map based on the motion model
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #(success, saliencyMap) = saliency.computeSaliency(gray)
        #saliencyMap = (saliencyMap * 255).astype("uint8")
        #print(success)

        #apply foreground segmentation
        fgMask = saliency.apply(frame, learningRate = 1/i)

        #add frame counter to original image
        cv2.rectangle(frame, (10, 2), (100,20), (255,255,255), -1)
        cv2.putText(frame, str(cap.get(cv2.CAP_PROP_POS_FRAMES)), (15, 15),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))

        #print to screen
        cv2.imshow("Image", frame)
        cv2.imshow("Salience", fgMask)

        # #save to file
        #cv2.imwrite(os.path.join(output_path,stimulus_name+"_motion_salience_frame"+str(i)+".jpg"), fgMask) #write salience map
        #print(os.path.join(output_path,stimulus_name+"_motion_salience"+str(i)+".jpg")) #print processed salience map

        i=i+1 #increase count

        keyboard = cv2.waitKey(30)
        if keyboard == 'q' or keyboard == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
