#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author:LMY
#time:2020/3/9

import cv2
import numpy as np

def findFace(img):
    # 加载人脸识别分类器
    faceCascade = cv2.CascadeClassifier(r'.\haarcascade_frontalface_default.xml')
    # 加载识别眼睛的分类器
    eyeCascade = cv2.CascadeClassifier(r'.\haarcascade_eye.xml')
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 人脸检测
    faces = faceCascade.detectMultiScale(img_grey, scaleFactor=1.2, minNeighbors=5)
    # 眼睛检测
    for (x, y, w, h) in faces:
        fac_grey = img_grey[y:(y+h), x:(x+w)]
        result = []
        eyes = eyeCascade.detectMultiScale(fac_grey, scaleFactor=1.2, minNeighbors=2)
        # 眼睛坐标的换算，相对坐标转换为绝对坐标
        for (ex, ey, ew, eh) in eyes:
            result.append((x+ex, y+ey, ew, eh))
    return faces, result

def rectangle(img, faces, result):
    # 在人脸上画矩形
    # (x,y)为人脸区域左上角坐标，w和h为矩形的宽和高
    if len(faces) > 0:
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
        for (ex, ey, ew, eh) in result:
            cv2.rectangle(img, (ex,ey), (ex+ew, ey+eh), (0,255,0), 2)
    cv2.imshow('img', img)



if __name__ == '__main__':
    img = cv2.imread('.\Test.png')
    faces, result = findFace(img)
    rectangle(img, faces, result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

