import cv2
import os
import numpy as np
from PIL import Image
from datetime import date
import pymsgbox

def Sort():
    today = date.today()
    # dd/mm/YY
    d1 = today.strftime("%d/%m/%Y")
    lines_seen = set() # holds lines already seen
    outfile = open("attendance.txt", "w+")
    for line in open("temp_attendance.txt", "r"):
        if line not in lines_seen: # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()
    os.remove("temp_attendance.txt")
    pymsgbox.alert('Attendance Sorted!', 'Alert')


def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

def getImagesAndLabels(path,detector):

    # Get all file path
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)] 
    
    # Initialize empty face sample
    faceSamples=[]
    
    # Initialize empty id
    ids = []

    # 
    for imagePath in imagePaths:

        # Get the image and convert it to grayscale
        PIL_img = Image.open(imagePath).convert('L')

        # PIL image to numpy array
        img_numpy = np.array(PIL_img,'uint8')

        # Get the image id
        id = (os.path.split(imagePath)[-1].split("."))
        id=int(id[1])

        # Get the face from the training images
        faces = detector.detectMultiScale(img_numpy)

        # Loop for each face, append to their respective ID
        for (x,y,w,h) in faces:

            # Add the image to face samples
            faceSamples.append(img_numpy[y:y+h,x:x+w])

            # Add the ID to IDs
            ids.append(id)

    return faceSamples,ids
def Capture(rollNo,Name):                       
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video width
    cam.set(4, 480) # set video height

    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # For each person, enter one numeric face id
    face_id = rollNo


    print("\n [INFO] Initializing face capture. Look the camera and wait ...")

    # Initialize individual sampling face count
    count = 0

    while(True):
        
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.05, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
            count += 1
            print(count)

            # Save the captured image into the datasets folder
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
            cv2.imshow('image', img)
        cv2.imshow('image', img)
        k = cv2.waitKey(1) & 0xff
        if k == 27:# Press 'ESC' for exiting video
            break
        elif count >= 15: # Take 30 face sample and stop video
            break


    fo=open("names.txt","a")
    fo.write(Name+"\n")
    fo.close()
    pymsgbox.alert('Hey {} you have been added to my database'.format(Name), 'Alert')
    print("\n [INFO] Exiting Program ")
    cam.release()
    cv2.destroyAllWindows()


def Train():
    recognizer = cv2.face.LBPHFaceRecognizer_create()    
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    faces,ids = getImagesAndLabels('dataset',detector)
    # Train the model using the faces and IDs
    recognizer.train(faces, np.array(ids))
    # Save the model into trainer.yml
    assure_path_exists('trainer/')
    recognizer.save('trainer/trainer.yml')
    pymsgbox.alert('Training Complete!', 'Alert')



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
            scaleFactor = 1.025,
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
            at=open("temp_attendance.txt","a")
            at.write('%d\t%s\n'%(l,id))
            at.close()
            pymsgbox.alert('{} you have been marked present ,Press Esc to quit!'.format(id), 'Alert')
        if k == 27:
            break

    # Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()

     
