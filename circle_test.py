import cv2
import numpy as np
"""
순서: 원만 찾기
    빨강색 찾기
    원이랑 빨강색 동시에 찾기 -> 흰색, 빨강색 범위에 있는 것들 mask 하기
    원 인식. 흰색 50퍼알 때 축구공으로 인식. 
"""

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

while True:
    retval, frame = cap.read()
    if not retval:
        break

    frame2 = frame.copy()
    frame_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    blr = cv2.GaussianBlur(frame_gray, (5, 5), 0)

    cv2.imshow('frame', frame)
    # cv2.imshow('mask', dst1)
    # cv2.imshow('mask2', dst2)

    # dst = cv2.add(dst1, dst2)
    # cv2.imshow('+', dst)
    # dst = cv2.GaussianBlur(dst, (3, 3), 0)
    circles1 = cv2.HoughCircles(blr, cv2.HOUGH_GRADIENT, 1, 20, param1=250, param2=30, minRadius=80, maxRadius=150)
    if circles1 is not None:
        for i in circles1[0]:
            i = i.astype(int)
            cx, cy, radius = i
            cv2.circle(blr, (cx, cy), radius, (0, 0, 255), 5)

    # dst_result = cv2.bitwise_and(frame, frame, mask=dst1)
    # cv2.imshow('dst1', dst_result)
    # dst_result2 = cv2.bitwise_and(frame, frame, mask=dst2)
    # cv2.imshow('dst2', dst_result2)
    # result = cv2.add(dst_result, dst_result2)
    # cv2.imshow('result', dst)
    cv2.imshow('original', blr)

    key = cv2.waitKey(25)
    if key == 27:
        break

if cap.isOpened():
    cap.release()
    cv2.destroyAllWindows()



