import cv2
import mediapipe as mp
import time

input = cv2.VideoCapture(0)

mpTangan = mp.solutions.hands
tangan = mpTangan()

while True:
    ret, img = input.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hasil = tangan.process(imgRGB)

    cv2.imshow("image", img)
    cv2.waitKey(1)