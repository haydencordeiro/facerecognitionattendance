# facerecognitionattendance
using  numpy  train peoples faces and use it for attendance by simply hitting space<br>

steps to use the project<br>
1 run the dataset python scrpt<br>
ensure each user has  a unique id <br>
ensure all the pictures stored in the dataset folder are clear<br>
run the reconition python script<br>
hit the enter key to mark the attendance<br>


Notes<br>
Incase the system is not detecting properly there could be an issue with the pictures in the dataset have a look thrugh the pictures and delete the blur ones <br>
Also ensure the ids match the user in the database folder<br>
Avoid using spectacles or caps while traning .<br>
Avoid moving around while tranning<br>
Ensure camera focuses on the face properly<br>


Incase of this eroror<br>
module 'cv2.cv2' has no attribute 'face'<br>
RUN:pip install opencv-contrib-python<br>
