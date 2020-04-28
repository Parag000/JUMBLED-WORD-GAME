import cv2
import numpy as np

def reddetect(frame): #FUNCTION TO DETECT COLOR
     img1 = cv2.inRange(frame,(0,0,120),(100,100,255))#BGR VALUE RANGE OBTAINED FROM A SAMPLE IMAGE
     img1 = img1/255#SINCE FUNCTION RETURNS 0 OR 255 WE DIVIDE IT BY 255 TO RECEIVE IT IN 0 AND 1'S
     s1 = np.sum(img1)
     dim1 = img1.shape
     mask1 = (s1/(dim1[0]*dim1[1]))
     
     if(mask1 > 0.05):#0.05 REPRESENTS PERCENTAGE[5%]
        return True   
     else:
        return False
 
def greendetect(frame):
    img2 = cv2.inRange(frame,(70,100,55),(100,255,100))
    img2 = img2/255
    s2 = np.sum(img2)
    dim2 = img2.shape
    mask2 = (s2/(dim2[0]*dim2[1]))
    
    if(mask2 > 0.008):
        return True
    else:
        return False

def bluedetect(frame):
    img3 = cv2.inRange(frame,(110,94,20),(255,130,80))
    cv2.imwrite('img3.png',frame)
    img3 = img3/255
    s3 = np.sum(img3)
    dim3 = img3.shape
    mask3 = (s3/(dim3[0]*dim3[1]))
    
    if(mask3 > 0.02):
        return True
    else:
        return False   
    
def redfilterframe(frame):#FUNCTION TO APPLY RED FILTER
    frame[:,:,0]=20#REDUCING INTENSITY OF OTHER TWO COLORS
    frame[:,:,1]=20
    return frame

def greenfilterframe(frame):#FUNCTION TO APPLY GREEN FILTER
    frame[:,:,0]=5
    frame[:,:,2]=5
    return frame

def bluefilterframe(frame):#FUNCTION TO APPLY BLUE FILTER
    frame[:,:,1]=10
    frame[:,:,2]=10


cap = cv2.VideoCapture(0)

while 1:

    ret,frame = cap.read()
    
    rec1 = reddetect(frame)
    rec2 = greendetect(frame)
    rec3 = bluedetect(frame)
    
    if(rec1==True):
        frame1 = redfilterframe(frame)
    
    if(rec2 == True):
        frame2 = greenfilterframe(frame)
        
    if(rec3 == True):
        frame3 = bluefilterframe(frame)
    
    cv2.imshow('frame',frame) 
 
    if cv2.waitKey(30)  & 0xFF == ord('q'):#INCREASE WAITKEY TO GET A CLICK EFFECT TO 2000
        break
 
cap.release()
cv2.destroyAllWindows()
