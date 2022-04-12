@echo off

ECHO Identify STATIC SALIENCE in VIDEO files:
ECHO INFO: splits video into images that are separately analyzed
ECHO -----------------------------------------------------

REM set /p path="Enter Path with Video files: "
set path="C:\Users\Nico\PowerFolders\data_LEAP\stimuli\nonhuman"
set /p name="Enter Name of the Video: "

REM e.g. path = "C:/Users/Nico/PowerFolders/Paper_AIMS-LEAP_ETcore/stimuli/nonhuman"
REM e.g. path = "birds"

REM independent of environment variables (full path files)

ECHO SPLITTING VIDEO...
"C:\Python38\python.exe" "C:\Users\Nico\PowerFolders\project_video_salience\split_video_to_images.py" %name% %path%
ECHO ...DONE

ECHO IDENTIFY SALIENCE...
"C:\Python38\python.exe" "C:\Users\Nico\PowerFolders\project_video_salience\static_salience_in_video.py" %name%
ECHO ...DONE

REM with environment variables
REM start "split_video" python split_video_to_images.py
REM start "salience_detection" python static_salience_in_video.py %name%

PAUSE
