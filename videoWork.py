<<<<<<< HEAD
import cv2
import numpy as np

new_capture = cv2.VideoCapture('fun.mp4') #place a video in the same directory

# Check if the file opened successfully
if(new_capture.isOpened()==False):
    print("Error in processing video file")

# Read the video
while(new_capture.isOpened()):
    ret, frame = new_capture.read()
    if ret == True:
        cv2.imshow('Frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

# Release when everything is done
new_capture.release()
cv2.destroyAllWindows() #close all frames
=======
import cv2
import numpy as np

new_capture = cv2.VideoCapture('fun.mp4') #place a video in the same directory

# Check if the file opened successfully
if(new_capture.isOpened()==False):
    print("Error in processing video file")

# Read the video
while(new_capture.isOpened()):
    ret, frame = new_capture.read()
    if ret == True:
        cv2.imshow('Frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

# Release when everything is done
new_capture.release()
cv2.destroyAllWindows() #close all frames
>>>>>>> 43db44dace037fabb8b1e1c0b48a080077a5e55a
