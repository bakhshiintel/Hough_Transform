import cv2 as cv
import numpy as np
img = cv.imread(cv.samples.findFile( 'road .jpeg' ))
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray,50,150,apertureSize = 3)
lines = cv.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)
print(lines)
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv.line(img,(x1,y1),(x2,y2),(0,255,0),2)
cv.namedWindow('hough_line',cv.WINDOW_NORMAL)
cv.imshow('hough_line',img)
cv.waitKey(0)
cv.destroyAllWindows()




