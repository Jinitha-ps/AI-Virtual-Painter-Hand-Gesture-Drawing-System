import cv2
import HandTrackingModule as htm
detector = htm.handDetector()
import numpy as np

# Creating image canvas
img_canvas =  np.zeros((720,1280,3),np.uint8)

cap = cv2.VideoCapture(0)
draw_color = (0,0,255)

# 💡 CORRECTION: Initialize xp and yp outside the loop 
xp, yp = 0, 0 

while True:
    x,img = cap.read()
    img = cv2.resize(img,(1280,720))
    img = cv2.flip(img,1)

#Draw rectangle (Color Palette/UI)
    img = cv2.rectangle(img,pt1=(10,100),pt2=(200,10),color=(0,0,255),thickness=-1)
    img = cv2.rectangle(img,pt1=(210,100),pt2=(400,10),color=(0,255,0),thickness=-1)  
    img = cv2.rectangle(img,pt1=(410,100),pt2=(600,10),color=(255,0,0),thickness=-1)
    img = cv2.rectangle(img,pt1=(610,100),pt2=(800,10),color=(0,255,255),thickness=-1)
    img = cv2.rectangle(img,pt1=(810,100),pt2=(1270,10),color=(255,255,255),thickness=-1)
    img = cv2.putText(img,text='ERASER',org=(1000,60),fontFace= cv2.FONT_HERSHEY_COMPLEX,fontScale= 1,
                       color= (0,0,0),
                       thickness=2)
    
    
#Detect hands
    img = detector.findHands(img)

#Finding the position of all landmarks
    lmlist = detector.findPosition(img)
    

    if len(lmlist)!=0:
        x1,y1 = lmlist[8][1:] #index finger tip coordinates
        x2,y2 = lmlist[12][1:] #middle finger tip coordinates
        #print(x1,y1)
        #print(x2,y2)
       


#Detect if fingers are up(two modes selection mode and drawing mode)
        fingers = detector.fingersUp()
        #print(fingers)  #1 ==>fingers up
                         #0 ==>fingers down
        
        
    
#Check if two fingers are up ==>Selection mode
        if fingers[1] and fingers[2]:
            #print("Selection mode")
            xp,yp = 0,0 # Set xp, yp to 0 to stop drawing when switching to selection

# To check the height of fingers and identify the colors           
            if y1<100:

                if 10<=x1<=200:   ## if red color occur in the range from above drawing rectangle condition.
                    print("Red")
                    draw_color = (0,0,255)

                elif 210<=x1<=400:   
                    print("Green")
                    draw_color = (0,255,0)

                elif 410<=x1<=600:
                    print("Blue")
                    draw_color = (255,0,0) 

                elif 610<=x1<= 800:
                    print("Yellow")
                    draw_color = (0,255,255)

                elif 810<=x1<=1270:
                    print("Eraser") 
                    draw_color = (0,0,0)        
                    

                

# When we choose a color, to fix the tip of two fingers are in choosed color
            cv2.rectangle(img,(x1,y1),(x2,y2),color=draw_color,thickness=-1)            
    
#Check if index finger is up==>Drawing mode
        if fingers[1] and not fingers[2]:
            #print("Drawing mode")

# To drawing a circle in fingertip
            cv2.circle(img,(x1,y1),15,draw_color,thickness=-1)  

#create a new rgb canvas to start drawing 
            if xp == 0 and yp == 0:
               xp = x1
               yp = y1
# colors
#For eraser different condition is passed since it is used to erase
            if draw_color == (0,0,0):
               cv2.line(img,(xp,yp),(x1,y1),color = draw_color,thickness = 50)#50 since it is used to erase
               cv2.line(img_canvas,(xp,yp),(x1,y1),color = draw_color,thickness = 50)#50 since it is used to erase


            else:
               cv2.line(img,(xp,yp),(x1,y1),color = draw_color,thickness = 15)
               cv2.line(img_canvas,(xp,yp),(x1,y1),color = draw_color,thickness = 15)
               
            xp,yp = x1,y1
    
#merges the canvas and frame (the one we already have)                       
            
# Image converted into image grey

    img_grey = cv2.cvtColor(img_canvas,cv2.COLOR_BGR2GRAY)        

# Image inversing
    _,img_inv = cv2.threshold(img_grey,20,255,cv2.THRESH_BINARY_INV)  # 20 is threshold values and 255 is maximum threshold value.

# Image inverse(ie,grey image) converted into BGR
    img_inv = cv2.cvtColor(img_inv,cv2.COLOR_GRAY2BGR) 

# AND & OR  operations (And opeartions occured in image & image operation, OR operation occured in image and image canvas operation)
    img = cv2.bitwise_and(img,img_inv)
    img = cv2.bitwise_or(img,img_canvas)

# Add two images
    img = cv2.addWeighted(img,1,img_canvas,0.5,0) #the values corresponding to alpha,beta,gamma    
          

            




    cv2.imshow('Virtual Painter',img)
    
    if cv2.waitKey(1) & 0xFF==27: # Press ESC to exit
        break

cap.release()
cv2.destroyAllWindows()