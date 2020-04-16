[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)                  [![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)          [![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)

using  numpy  train peoples faces and use it for attendance by simply hitting space<br>

steps to use the project<br>
Install all requirements by running pip install -r requirements.txt<br>
1 run the dataset python scrpt<br>
ensure each user has  a unique id <br>
ensure all the pictures stored in the dataset folder are clear<br>
run the reconition python script<br>
hit the enter key to mark the attendance<br>


Notes<br>
Start The First Id By 0<br>
Incase the system is not detecting properly there could be an issue with the pictures in the dataset have a look thrugh the pictures and delete the blur ones <br>
Also ensure the ids match the user in the database folder<br>
Avoid using spectacles or caps while traning .<br>
Avoid moving around while tranning<br>
Ensure camera focuses on the face properly<br>


Incase of this eroror<br>
module 'cv2.cv2' has no attribute 'face'<br>
RUN:pip install --force-reinstall opencv-contrib-python==4.1.2.30
