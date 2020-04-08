import cv2
import os
import numpy as np
from PIL import Image
 
 


def GetImages(name,rollNo): #Get user Images                
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video width
    cam.set(4, 480) # set video height
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # For each person, enter one numeric face id
    face_id = rollNo


    print("\nLook the camera and wait ...")

    # Initialize individual sampling face count
    count = 0
    while(True):
        
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.05, 5)

        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
            count += 1
            # Save the captured image into the datasets folder
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
            cv2.imshow('image', img)

        k = cv2.waitKey(1) & 0xff
        if k == 27:# Press 'ESC' for exiting video
            break
        elif count >= 50: # Take 30 face sample and stop video
            break


    fo=open("names.txt","a")
    fo.write(name+"\n")
    fo.close()
    print("\n [INFO] Exiting Program ")
    cam.release()
    cv2.destroyAllWindows()



def Recognise():
    fo= open("names.txt","r")
    names=fo.readlines()
    fo.close()
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);

    font = cv2.FONT_HERSHEY_SIMPLEX

    #iniciate id counter
    id = 0


    # Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video widht
    cam.set(4, 480) # set video height

    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)

    while True:

        ret, img =cam.read()
        

        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
           )
        
        for(x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 4)

            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
               
            # Check if confidence is less them 100 ==> "0" is perfect match 
            if (confidence < 100):
                l=id
                id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))
            else:
                id = "...."
                confidence = "  {0}%".format(round(100 - confidence))
            
            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
        
        cv2.imshow('camera',img)
       
        
        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        if k == 32:
            at=open("attendance.txt","a")
            at.write('%d\t%s\n'%(l,id))
            at.close()
        if k == 27:
            break
        
    # Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()

     
def RemoveMultipleEnteries():
	f=open('attendance.txt','r+')
	List=f.readlines()
	f.close()
	Set=set(List)
	string=''
	for ele in Set:
		string+=ele
	f=open('attendance.txt','w')
	f.write(string)
	f.close()

