import cv2
import mediapipe as mp
import time

input = cv2.VideoCapture(0)

mpTangan = mp.solutions.hands
tangan = mpTangan.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    ret, img = input.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hasil = tangan.process(imgRGB)
    print(hasil.multi_hand_landmarks)

    if hasil.multi_hand_landmarks:
        for tanganKu in hasil.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, tanganKu)

    cv2.imshow("image", img)
    cv2.waitKey(1)