# Import opencv
import cv2 
# Import uuid
import uuid
# Import Operating System
import os
# Import time
import time

# 2. Define Images to Collect
labels = ['ar1', 'ar2', 'ar3', 'ar4', 'ar5', 'ar6', 'ar7', 'ar8', 'ar9']

# 3. Setup Folders 
IMAGES_PATH = os.path.join("Tensorflow","collectedimages")
if not os.path.exists(IMAGES_PATH):
    os.makedirs (IMAGES_PATH )

for label in labels:
    path = os.path.join(IMAGES_PATH, label)
    if not os.path.exists(path):
        os.mkdir (path)

## 4. Capture Images
k=0
cap = cv2.VideoCapture(0)
cv2.namedWindow("Python zeed capturar imagenes")
number_imgs = 20
for label in labels:
    print('Collecting images for {}'.format(label))
    for imgnum in range(number_imgs):
        while True:
            ret,frame = cap.read()
            if ret:
                cv2.imshow("test",frame)
                k = cv2.waitKey(1)
                if k%256 == 27:
                    print ("Escape hit, closing the app")
                    break
                elif k%256 == 32:
                    imgname = os.path.join(IMAGES_PATH,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
                    cv2.imwrite(imgname, frame)
                    print('Collecting image {}'.format(imgnum))
                    break
        if k%256 == 27:
            print ("Escape hit, closing the app")
            break
    if k%256 == 27:
        print ("Escape hit, closing the app")
        break
cap.release()
cap.destroyAllWindows()