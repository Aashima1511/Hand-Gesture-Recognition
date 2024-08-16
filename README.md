# Hand-Gesture-Recognition
The project aims to perform the basic functionalities of a pc without using a keyboard and mouse. 

## Objectives
1. Accuracy
2. Real-time Processing
3. Robustness
4. Privacy
5. Accessibility

## Libraries used
1. OpenCv
2. Mediapipe
3. PyAutoGUI
4. Scree Brightness Control
5. hypot from math

## Steps involved
1. Import necessary libraries
2. Initialize the hand model from MediaPipe library and start capturing from the webcam.
3. Read the video frame by frame and flip the image horizontally.
4. Convert BGR image to RGB for compatibility with MediaPipe.
5. If the hand is present then landmarks are drawn.

## Functions performed
1. volume control function
2. brightness control function
3. zoom control function
4. scroll control function
