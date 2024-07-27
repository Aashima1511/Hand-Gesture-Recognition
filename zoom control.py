# Importing Libraries 
import cv2 
import mediapipe as mp
import pyautogui
from math import hypot 
import numpy as np 


# Initializing the Model 
mpHands = mp.solutions.hands 
hands = mpHands.Hands( 
    static_image_mode=False, 
    model_complexity=1, 
    min_detection_confidence=0.75, 
    min_tracking_confidence=0.75, 
    max_num_hands=1) 

Draw = mp.solutions.drawing_utils


def manage_zoom(landmarkList):
    x_1, y_1 = landmarkList[4][1], landmarkList[4][2]
    # store x,y coordinates of (tip of) ring finger 
    x_2, y_2 = landmarkList[16][1], landmarkList[16][2] 
    # draw circle on thumb and ring finger tip 
    cv2.circle(frame, (x_1, y_1), 7, (0, 255, 0), cv2.FILLED) 
    cv2.circle(frame, (x_2, y_2), 7, (0, 255, 0), cv2.FILLED)
    # draw line from tip of thumb to tip of ring finger
    distance= hypot(x_2-x_1, y_2-y_1)
    zoom_level = int(distance * 100 / 100)
    cv2.line(frame, (x_1, y_1), (x_2, y_2), (0, 255, 0), 3)
    if zoom_level > 50:
        pyautogui.hotkey('ctrl', '+')
    else:
        pyautogui.hotkey('ctrl', '-')


# Start capturing video from webcam 
webcam = cv2.VideoCapture(0) 

while True: 
    # Read video frame by frame 
    _, frame = webcam.read() 

    # Flip image 
    frame = cv2.flip(frame, 1)


    # Convert BGR image to RGB image 
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 

    # Process the RGB image 
    Process = hands.process(frameRGB) 

    landmarkList = [] 
    # if hands are present in image(frame) 
    if Process.multi_hand_landmarks: 
        # detect handmarks 
        handlm = Process.multi_hand_landmarks[0]
        for _id, landmarks in enumerate(handlm.landmark): 
            # store height and width of image 
            height, width, color_channels = frame.shape 
            # calculate and append x, y coordinates 
            # of handmarks from image(frame) to lmList 
            x, y = int(landmarks.x*width), int(landmarks.y*height) 
            landmarkList.append([_id, x, y]) 

        # draw Landmarks 
        Draw.draw_landmarks(frame, handlm, mpHands.HAND_CONNECTIONS)
        
    if landmarkList != []:
        manage_zoom(landmarkList)

    # Display Video and when 'esc' is entered, destroy 
    # the window 
    cv2.imshow('Image', frame) 
    key=cv2.waitKey(10)
    if key==27:
        break

webcam.release()
cv2.destroyAllWindows()
