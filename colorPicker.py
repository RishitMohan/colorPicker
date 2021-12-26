import cv2
import numpy as np
def nothing(x):
    pass
#blank
img=np.zeros((300,512,3),np.uint8)
cv2.namedWindow(winname="color picker")

#switch
s1= "0:OFF \n 1:ON"
cv2.createTrackbar(s1,"color picker",0,1,nothing)

#Manage colors
cv2.createTrackbar("R","color picker",0,255,nothing)
cv2.createTrackbar("G","color picker",0,255,nothing)
cv2.createTrackbar("B","color picker",0,255,nothing)




while True:
        #trackbar pos
    s=cv2.getTrackbarPos(s1,"color picker")
    r=cv2.getTrackbarPos("R","color picker")
    g=cv2.getTrackbarPos("G","color picker")
    b=cv2.getTrackbarPos("B","color picker")
    print("r:"+str(r)," g:"+str(g)+" b " +str(b))
    if s==0:
        img[:]=0
    else:
        img[:]=[r,g,b]     




    cv2.imshow("color picker",img)
    k=cv2.waitKey(1)
    if k==27:
        break




