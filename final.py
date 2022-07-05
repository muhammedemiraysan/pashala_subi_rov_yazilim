def nothing(x):
    pass 
from hashlib import shake_128
import cv2
import numpy as np
import serial
import time
from msvcrt import getch
import pyfirmata
import pygame
pygame.init()
width, height = 20, 20
screen = pygame.display.set_mode((width, height))
board = pyfirmata.Arduino('COM25')
print("Communication Successfully started")
servo1 = board.get_pin('d:6:s')
servo2 = board.get_pin('d:3:s')
servo3 = board.get_pin('d:5:s')
servo4 = board.get_pin('d:10:s')
servo5 = board.get_pin('d:9:s')
servo6 = board.get_pin('d:7:s')
servo7 = board.get_pin('d:11:s')
kamera_servo = board.get_pin('d:8:s')
servo1a = 0
servo1b = 0
servo2c = 0
servo3a = 0
servo3b = 0
servo4a = 0
servo4b = 0
servo5c = 0
servo6a = 0
servo6b = 0
servo7a = 0
cap = cv2.VideoCapture(1)
img = np.zeros((300,500,3), np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('low_b','image',0,255,nothing)
cv2.createTrackbar('low_g','image',0,255,nothing)
cv2.createTrackbar('low_r','image',0,255,nothing)
cv2.createTrackbar('high_b','image',0,255,nothing)
cv2.createTrackbar('high_g','image',0,255,nothing)
cv2.createTrackbar('high_r','image',0,255,nothing)
cv2.createTrackbar('erosion','image',0,10,nothing)
cv2.createTrackbar('dilation','image',0,10,nothing)
cv2.createTrackbar('kamera_servo','image',0,180,nothing)
cv2.createTrackbar('ana_motor_hiz','image',0,100,nothing)
cv2.createTrackbar('r','image',0,100,nothing)
servo1.write(1470)
servo2.write(1470)
servo3.write(1470)
servo4.write(1470)
servo5.write(1470)
servo6.write(1470)
servo7.write(1470)
kamera_servo.write(1470)
cv2.setTrackbarPos('low_b','image',30)
cv2.setTrackbarPos('low_g','image',150)
cv2.setTrackbarPos('low_r','image',50)
    
cv2.setTrackbarPos('high_b','image',255)
cv2.setTrackbarPos('high_g','image',255)
cv2.setTrackbarPos('high_r','image',180)
cv2.setTrackbarPos('erosion','image',8)
cv2.setTrackbarPos('ana_motor_hiz','image',50)
cv2.setTrackbarPos('kamera_servo','image',90)
cv2.setTrackbarPos('r','image',0)
time.sleep(7)
while cap.isOpened():
    ret,image = cap.read()
    h1 = cv2.getTrackbarPos('low_b',"image")
    h2 = cv2.getTrackbarPos('low_g',"image")
    h3 = cv2.getTrackbarPos('low_r',"image")
    s1 = cv2.getTrackbarPos('high_b',"image")
    s2 = cv2.getTrackbarPos('high_g',"image")
    s3 = cv2.getTrackbarPos('high_r',"image")
    it1 = cv2.getTrackbarPos('erosion',"image")
    it2 = cv2.getTrackbarPos('dilation',"image")
    ana_hiz = cv2.getTrackbarPos('ana_motor_hiz','image')
    r = cv2.getTrackbarPos('r','image')
    #ust_motor_hiz= (cv2.getTrackbarPos('ust_motor_hiz','image') )
    #motor7_hiz = (cv2.getTrackbarPos('motor7_hiz','image') )
    #ust_motor_hiza= (cv2.getTrackbarPos('ust_motor_hiza','image') )
    #motor7_hiza = (cv2.getTrackbarPos('motor7_hiza','image') )
    kameraa = cv2.getTrackbarPos('kamera_servo','image')
    #servo2c = ust_motor_hiz 
    #servo5c = ust_motor_hiz 
    #servo7a = motor7_hiz + motor7_hiza
     #p1 = int(cv2.getTrackbarPos('param1', 'hc'))
     #p2 = int(cv2.getTrackbarPos('param2', 'hc'))
     #minrad = cv2.getTrackbarPos('MinRad', 'hc')
     #maxrad = cv2.getTrackbarPos('MaxRad', 'hc')
     #esik1 = cv2.getTrackbarPos('1.esik', 'hc')
     #esik2 = cv2.getTrackbarPos('2.esik', 'hc')
     #canny1 = int(cv2.getTrackbarPos('canny1','hc'))
     #canny2 = int(cv2.getTrackbarPos('canny2','hc'))

    colorLower = np.array([h1, h2, h3]) 
    colorUpper = np.array([s1, s2, s3]) 
    (qwert, frame) = cap.read()

    frameForHC = frame
    frameForUser = frame
     
    frame = cv2.resize(frame, (int(height), int(width))) 
    frameForHC = cv2.resize(frameForHC, (int(height), int(width)))
    frameForUser = cv2.resize(frameForUser, (int(height), int(width)))
     

    cv2.line(frameForUser, (0, int(width/3)) , (int(height), int(width/3)), (0,0,0), 3)
    #cv2.line(frameForHC, (0, int(width/3)) , (int(height), int(width/3)), (0,0,0), 3)
    cv2.line(frameForUser, (0, int((width/3)*2)) , (int(height), int((width/3)*2)), (0,0,0), 3)
    #cv2.line(frameForHC, (0, int((width/3)*2)) , (int(height), int((width/3)*2)), (0,0,0), 3)
    cv2.line(frameForUser, (int(height/3), 0) ,(int(height/3), int(width)), (0,0,0), 3)
    #cv2.line(frameForHC, (int(height/3), 0) ,(int(height/3), int(width)), (0,0,0), 3)
    cv2.line(frameForUser, (int((height/3)*2), 0) ,(int((height/3)*2), int(width)), (0,0,0), 3)
    #cv2.line(frameForHC, (int((height/3)*2), 0) ,(int((height/3)*2), int(width)), (0,0,0), 3)
    cv2.line(frameForUser, (int((height/3)+80), int((width/3)+40)),(int(((height/3)*2)-80), int((width/3)+40)),(0,0,0),3)
    #cv2.line(frameForHC, (int((height/3)+80), int((width/3)+40)),(int(((height/3)*2)-80), int((width/3)+40)),(0,0,0),3)
    cv2.line(frameForUser, (int(((height/3)*2)-80), int((width/3)+40)), (int(((height/3)*2)-80), int(((width/3)*2)-40)), (0,0,0), 3)
    #cv2.line(frameForHC, (int(((height/3)*2)-80), int((width/3)+40)), (int(((height/3)*2)-80), int(((width/3)*2)-40)), (0,0,0), 3)
    cv2.line(frameForUser, (int((height/3)+80), int(((width/3)*2)-40)), (int(((height/3)*2)-80), int(((width/3)*2)-40)), (0,0,0), 3)
    #cv2.line(frameForHC, (int((height/3)+80), int(((width/3)*2)-40)), (int(((height/3)*2)-80), int(((width/3)*2)-40)), (0,0,0), 3)
    cv2.line(frameForUser,(int((height/3)+80), int((width/3)+40)), (int((height/3)+80), int(((width/3)*2)-40)), (0,0,0), 3)
    #cv2.line(frameForHC,(int((height/3)+80), int((width/3)+40)), (int((height/3)+80), int(((width/3)*2)-40)), (0,0,0), 3)
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #gray = cv2.cvtColor(canny, cv2.COLOR_BGR2GRAY)

    #görüntü iyileştirme:

    medianblured = cv2.medianBlur(hsv, 7)

    #frameForHC = cv2.bilateralFilter(frameForHC, 50 , 75 , 75)
    bilateralfiltered = cv2.bilateralFilter(medianblured, 9 , 75 , 75)

    guassianblured = cv2.GaussianBlur(bilateralfiltered ,(5,5),0)

    #canny = cv2.Canny(frameForHC,40,40)

    kernel = np.ones((5,5),np.float32)/25

    #frameForHC = cv2.erode(canny, kernel, iterations=it1) 
    #frameForHC = cv2.dilate(canny, kernel, iterations=2) 

    #------------

    mask = cv2.inRange(hsv, colorLower, colorUpper) 
     
     #circles = cv2.HoughCircles(canny, cv2.HOUGH_GRADIENT, 1 ,150 ,param1=50,param2=30,minRadius=100,maxRadius=400) 
     #circles = np.uint16(np.around(circles))

     #kernel = np.ones((5,5),np.float32)/25
    mask = cv2.erode(mask, kernel, iterations=it1) 
    mask = cv2.dilate(mask, kernel, iterations=it2) 

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2] 
    center = None
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)

        if radius > r:
            try:

                M = cv2.moments(c)

                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
            except:
                pass
            if((x<(height/3)) and (y<(width/3))):
                hedef = 1
                print("1. konumda")

            elif(((x<((height/3)*2)) and (x > (height/3))) and (y<(width/3))):
                hedef = 2
                print("2. konumda")

            elif(((x<height) and (x > ((height/3)*2)) and (y<(width/3)))):
                hedef = 3
                print("3. konumda")

            elif((x<(height/3)) and (y>(width/2) and (y < ((width/3)*2))) ):
                hedef = 4
                print("4.konumda")

            elif(((x<((height/3)*2)) and (x > (height/3))) and (y>(width/3) and (y < ((width/3)*2)))):
                hedef = 5
                print("5. konumda")
                
            elif ((x<height) and (x > ((height/3)*2)) and (y>(width/3) and (y < ((width/3)*2)))):
                hedef = 6
                print("6. konumda")

            elif ((x<(height/3)) and ((y > ((width/3)*2)) and (y < width))):
                hedef = 7
                print("7. konumda")

            elif (((x<((height/3)*2)) and (x > (height/3))) and ((y > ((width/3)*2)) and (y < width))):
                hedef = 8
                print("8. konumda")

            elif (((x<height) and (x > ((height/3)*2)),) and ((y > ((width/3)*2)) and (y < width)) ):
                hedef = 9
                print("9. konumda")
            print("x : ",int(cx) ," , ","y : ", int(cy), " , ", "çap : ",radius)
            cv2.line(frame,(int(x-(radius)), int(y)), (int(x+(radius)), int(y)), (0,0,255), 2)
            #print(circles)

            cv2.putText(frame, ".", (int(cx), int(cy)), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,0), 3)
            cv2.putText(frameForUser, ".", (int(cx), int(cy)), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,0), 3)
            
            if radius > r: 
                
                cv2.circle(frame, (int(x), int(y)), int(radius),
                (255, 255, 255), 3)

                cv2.circle(frameForUser, (int(x), int(y)), int(radius),
                (255, 255, 255), 3)  
                
                #for i in circles[0,:]:
                    #cv2.circle(frameForHC,(i[0],i[1]),i[2],(0,255,0),2)
                    #cv2.circle(frameForHC,(i[0],i[1]),2,(0,0,255),3)

                    #cv2.circle(frameForUser,((i[0],i[1])),(i[2]),(0,255,0),2)
                    #cv2.circle(frameForUser,((i[0],i[1])),2,(0,0,255),3)

    cv2.imshow("color detection",frame)
    cv2.imshow("whiteblack",mask)
    #cv2.imshow("houghcircle", frameForHC)
    cv2.imshow("frameforuser",frameForUser)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("ğ"):
        exit()
    screen.fill((20, 20, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYUP:
            servo1a = 0
            servo3a = 0 
            servo4a = 0
            servo6a = 0
            servo1b = 0
            servo3b = 0 
            servo4b = 0
            servo6b = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        servo1a = 300
        servo3a = 300
        servo4a = 300
        servo6a = 300
        if keys[pygame.K_a]:
            servo1b = 300
            servo3b = -300
            servo4b = -300

            servo6b = -300
        if keys[pygame.K_d]:
            servo1b = -300
            servo3b = 300
            servo4b = 300
            servo6b = 300
    elif keys[pygame.K_a]:
        servo1b = 300
        servo3b = -300
        servo4b = -300
        servo6b = -300
    elif keys[pygame.K_d]:
        servo1b = -300
        servo3b = 300
        servo4b = 300
        servo6b = 300
    elif keys[pygame.K_s]:
        servo1a = -300
        servo3a = -300 
        servo4a = -300
        servo6a = -300
    elif keys[pygame.K_q]:
        servo2c = 400
        servo5c = 400
    elif keys[pygame.K_e]:
        servo2c = -400
        servo5c = -400
    elif keys[pygame.K_r]:
        servo2c = 0
        servo5c = 0
    elif keys[pygame.K_k]:
        servo7a = 300
    elif keys[pygame.K_l]:
        servo7a = -300
    elif keys[pygame.K_o]:
        servo7a = 0
    finalservo1 = 1470+((servo1a+servo1b)*(ana_hiz/100))
    finalservo3 = 1470+(((-1*servo3a)+(servo3b))*ana_hiz/100)
    finalservo4 = 1470+((servo4a+servo4b)*ana_hiz/100)
    finalservo6 = 1470+(((servo6a)+(servo6b))*ana_hiz/100)
    if finalservo1 > 1800:     
        finalservo1 = 1800
    if finalservo3 > 1800:
        finalservo3 = 1800
    if finalservo4 > 1800:
        finalservo4 = 1800
    if finalservo6 > 1800:
        finalservo6 = 1800
    if finalservo1 < 1100:
        finalservo1 = 1100
    if finalservo3 < 1100:
        finalservo3 = 1100
    if finalservo4 < 1100:
        finalservo4 = 1100
    if finalservo6< 1100:
        finalservo6 = 1100
    servo1.write(finalservo1)
    servo2.write(1470+(servo2c))   
    servo3.write(finalservo3)
    servo4.write(finalservo4)
    servo5.write(1470+(servo2c))
    servo6.write(finalservo6)
    servo7.write(1470+(servo7a))
    kamera_servo.write(kameraa)
    #print("servo1",1470+((servo1a+servo1b)*(ana_hiz/100))," servo2",1470+(servo2c*(ust_motor_hiz/100))," servo3",1470+(((-1*servo3a)+(servo3b))*ana_hiz/100)," servo4",1470+((servo4a+servo4b)*ana_hiz/100)," servo5",1470+((servo5c)*ust_motor_hiz/100)," servo6",1470+(((servo6a)+(servo6b))*ana_hiz/100)," servo7",1470+((servo7a)*motor7_hiz/100))
    pygame.display.flip()
