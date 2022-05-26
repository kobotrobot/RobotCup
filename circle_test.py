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
    # roi1
    x1 = 0
    y1 = 0
    w1 = 640
    h1 = 360
    roi1 = blr[y1:y1+h1, x1:x1+w1]

    # roi2
    x2 = 640
    y2 = 0
    w2 = 640
    h2 = 360
    roi2 = blr[y2:y2+h2, x2:x2+w2]

    # roi3
    x3 = 0
    y3 = 360
    w3 = 640
    h3 = 360
    roi3 = blr[y3:y3+h3, x3:x3+w3]

    # roi4
    x4 = 640
    y4 = 360
    w4 = 640
    h4 = 360
    roi4 = blr[y4:y4+h4, x4:x4+w4]

    cv2.imshow('frame', frame)
    # cv2.imshow('mask', dst1)
    # cv2.imshow('mask2', dst2)
    # dst = cv2.add(dst1, dst2)
    # cv2.imshow('+', dst)
    # dst = cv2.GaussianBlur(dst, (3, 3), 0)
    circles1 = cv2.HoughCircles(roi1, cv2.HOUGH_GRADIENT, 1, 20, param1=250, param2=30, minRadius=80, maxRadius=150)
    if circles1 is not None:
        for i in circles1[0]:
            print(1)
            i = i.astype(int)
            cx, cy, radius = i
            cv2.circle(roi1, (cx, cy), radius, (0, 0, 255), 5)

    circles2 = cv2.HoughCircles(roi2, cv2.HOUGH_GRADIENT, 1, 20, param1=250, param2=30, minRadius=80, maxRadius=150)
    if circles2 is not None:
        for i in circles2[0]:
            print(2)
            i = i.astype(int)
            cx, cy, radius = i
            cv2.circle(roi2, (cx, cy), radius, (0, 0, 255), 5)

    circles3 = cv2.HoughCircles(roi3, cv2.HOUGH_GRADIENT, 1, 20, param1=250, param2=30, minRadius=80, maxRadius=150)
    if circles3 is not None:
        for i in circles3[0]:
            print(3)
            i = i.astype(int)
            cx, cy, radius = i
            cv2.circle(roi3, (cx, cy), radius, (0, 0, 255), 5)

    circles4 = cv2.HoughCircles(roi4, cv2.HOUGH_GRADIENT, 1, 20, param1=250, param2=30, minRadius=80, maxRadius=150)
    if circles4 is not None:
        for i in circles4[0]:
            print(4)
            i = i.astype(int)
            cx, cy, radius = i
            cv2.circle(roi4, (cx, cy), radius, (0, 0, 255), 5)

    # if circles1
    # dst_result = cv2.bitwise_and(frame, frame, mask=dst1)
    # cv2.imshow('dst1', dst_result)
    # dst_result2 = cv2.bitwise_and(frame, frame, mask=dst2)
    # cv2.imshow('dst2', dst_result2)
    # result = cv2.add(dst_result, dst_result2)
    # cv2.imshow('result', dst)

    cv2.imshow('original', blr)
    cv2.imshow('roi1', roi1)
    cv2.imshow('roi2', roi2)
    cv2.imshow('roi3', roi3)
    cv2.imshow('roi4', roi4)

    key = cv2.waitKey(25)
    if key == 27:
        break

if cap.isOpened():
    cap.release()
    cv2.destroyAllWindows()
