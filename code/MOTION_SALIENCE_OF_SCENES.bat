"C:\Users\Nico\AppData\Local\Programs\Python\Python37\python.exe"@echo off

ECHO Identify MOTION SALIENCE of SCENES:
ECHO INFO: scenes are previously split by split_images_to_scenes.py...
ECHO -----------------------------------------------------

REM independent of environment variables (full path files)
REM path_to_python = where py

ECHO IDENTIFY MOTION SALIENCE...
"C:\Users\Nico\AppData\Local\Programs\Python\Python37\python.exe" "C:\Users\Nico\PowerFolders\project_video_salience\motion_salience_in_video_MOG2.py" 50faces
ECHO 50faces DONE
"C:\Users\Nico\AppData\Local\Programs\Python\Python37\python.exe" "C:\Users\Nico\PowerFolders\project_video_salience\motion_salience_in_video_MOG2.py" artist
ECHO artist DONE
"C:\Users\Nico\AppData\Local\Programs\Python\Python37\python.exe" "C:\Users\Nico\PowerFolders\project_video_salience\motion_salience_in_video_MOG2.py" birds
ECHO birds DONE
"C:\Users\Nico\AppData\Local\Programs\Python\Python37\python.exe" "C:\Users\Nico\PowerFolders\project_video_salience\motion_salience_in_video_MOG2.py" coralreef
ECHO coralreef DONE
"C:\Users\Nico\AppData\Local\Programs\Python\Python37\python.exe" "C:\Users\Nico\PowerFolders\project_video_salience\motion_salience_in_video_MOG2.py" dollhouse
ECHO dollhouse DONE
"C:\Users\Nico\AppData\Local\Programs\Python\Python37\python.exe" "C:\Users\Nico\PowerFolders\project_video_salience\motion_salience_in_video_MOG2.py" flowersstars
ECHO flowersstars DONE
"C:\Users\Nico\AppData\Local\Programs\Python\Python37\python.exe" "C:\Users\Nico\PowerFolders\project_video_salience\motion_salience_in_video_MOG2.py" musicbooth
ECHO musicbooth DONE
"C:\Users\Nico\AppData\Local\Programs\Python\Python37\python.exe" "C:\Users\Nico\PowerFolders\project_video_salience\motion_salience_in_video_MOG2.py" Pingu_doctors
ECHO Pingu_doctors DONE
"C:\Users\Nico\AppData\Local\Programs\Python\Python37\python.exe" "C:\Users\Nico\PowerFolders\project_video_salience\motion_salience_in_video_MOG2.py" Pingu1
ECHO Pingu1 DONE

PAUSE
