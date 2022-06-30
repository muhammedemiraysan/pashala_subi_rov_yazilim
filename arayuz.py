'''''''''import serial
import time
arac_arduino = serial.Serial(port="COM7",baudrate = 9600)
kumanda_arduino = serial.Serial(port="COM9",baudrate = 9600)
time.sleep(2)
while True:
    x = kumanda_arduino.readline()
    if x is not None:
        arac_arduino.write(bytes(str(x), 'utf-8'))
        print(x)'''''''''''
import serial
import time
import numpy as np 
import cv2



def nothing(): 
    pass    
arac_arduino = serial.Serial(port="COM7",baudrate = 9600)
kumanda_arduino = serial.Serial(port="COM9",baudrate = 9600)
time.sleep(2)
cv2.namedWindow('image')
cv2.createTrackbar('h1','image',0,360,nothing)
cv2.createTrackbar('h2','image',0,255,nothing)
cv2.createTrackbar('h3','image',0,255,nothing)
cv2.createTrackbar('s1','image',0,360,nothing)
cv2.createTrackbar('s2','image',0,255,nothing)   
cv2.createTrackbar('s3','image',0,255,nothing)
cv2.createTrackbar('it1','image',0,15,nothing)
cv2.createTrackbar('it2','image',0,15,nothing)
cv2.createTrackbar('r','image',0,500,nothing)  

height = 640 
width = 360

camera = cv2.VideoCapture(0) 

while True:
    h1 = cv2.getTrackbarPos('h1', 'image') 
    h2 = cv2.getTrackbarPos('h2', 'image')
    h3 = cv2.getTrackbarPos('h3', 'image')

    s1 = cv2.getTrackbarPos('s1','image')
    s2 = cv2.getTrackbarPos('s2','image')   
    s3 = cv2.getTrackbarPos('s3','image')

    it1 = cv2.getTrackbarPos('it1','image')
    it2 = cv2.getTrackbarPos('it2','image')
     
    r = cv2.getTrackbarPos('r','image')

    colorLower = np.array([h1, h2, h3]) 
    colorUpper = np.array([s1, s2, s3]) 

    (qwert, frame) = camera.read()
    frame = cv2.resize(frame, (height, width)) 
     
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  
    mask = cv2.inRange(hsv, colorLower, colorUpper) 
     
    kernel = np.ones((5,5),np.float32)/25
    mask = cv2.erode(mask, kernel, iterations=it1) 
    mask = cv2.dilate(mask, kernel, iterations=it2) 

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2] 

    center = None
    if len(cnts) > 0:
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            if radius > 50:
                M = cv2.moments(c)
                cx = (int(M["m10"])/int(M["m00"]))
                cy = (int(M["m01"])/int(M["m00"]))
                print("x değeri : ",cx ," , ","y değeri : ", cy, " , ", "Çap " , radius)
                cv2.putText(frame, ".", (int(cx), int(cy)), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,0), 3)
                if radius > r: 
                    cv2.circle(frame, (int(x), int(y)), int(radius),
                    (255, 255, 255), 3) 

    cv2.imshow("a",frame)
    cv2.imshow("b",mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()
