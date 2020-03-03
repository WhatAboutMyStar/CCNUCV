import cv2
import numpy as np
import matplotlib.pyplot as plt

global point1 , point2
global frame
def drawHist(p1,p2):
    img = frame[p1[1]:p2[1],p1[0]:p2[0],:]
    cv2.imshow("img",img)
    plt.hist(img.ravel(),256)
    plt.show()

def getHist(event,x,y,flags,param):
    global point1 , point2
    """
    point1  point3
    point4  point2
    """
    #从左上角到右下角拖一个矩形出来，矩形内的图片就是我们要的。
    if event == cv2.EVENT_LBUTTONDOWN:
        point1 = (x,y)
    elif event == cv2.EVENT_LBUTTONUP:
        point2 = (x,y)
        drawHist(point1,point2)

cap = cv2.VideoCapture('viptrain.avi')
cv2.namedWindow('callback')
cv2.setMouseCallback('callback',getHist)

while cap.isOpened():
    ret , frame = cap.read()
    cv2.imshow("callback",frame)
    key = cv2.waitKey()
    if key == 27: #ESC键退出，其他键继续播放视频。
        break
cap.release()
cv2.destroyAllWindows()
