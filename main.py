from sre_constants import SUCCESS
from tkinter.tix import IMAGE
import cv2
import time
import mediapipe as mp 
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

from xyz import BaseOptions 

base = python.BaseOptions
HandLandmarker = vision.HandLandmarker
HandLandmarkerOptions = vision.HandLandmarkerOptions
VisionRunningMode = vision.RunningMode

options = HandLandmarkerOptions(
    base_options = BaseOptions(model_asset_path = "hand_landmarker.task"),
    running_mode = VisionRunningMode.IMAGE,
    num_hands = 2
)

detector = HandLandmarker.creat_from_options(options)

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()


    cv2.imshow("Sign Language", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()