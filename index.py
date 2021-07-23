import cv2
import mediapipe as mp
import time

input = cv2.VideoCapture(0)

while True:
    success, img = input.read()

    cv2.imshow("image", img)
    cv2.waitKey(1)