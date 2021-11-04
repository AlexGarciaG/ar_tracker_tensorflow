#!/usr/bin/env python3
from __future__ import print_function

from numpy.core.fromnumeric import size

import roslib
roslib.load_manifest('ar_tracker_tensorflow')
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
# Import uuid
import uuid
# Import Operating System
import os
# Import time
import time



class image_converter:

  def __init__(self):
    #self.image_pub = rospy.Publisher("image_topic_2",Image)

    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/camera/color/image_raw",Image,self.callback)
    # 2. Define Images to Collect
    self.labels = ['ar3', 'ar4']
    self.label       = 0
    self.imgnum      = 0
    self.number_imgs = 20
    # 3. Setup Folders 
    self.images_path = os.path.join("Tensorflow","collectedimages")
    if not os.path.exists(self.images_path):
        os.makedirs (self.images_path )

    for label in self.labels:
        path = os.path.join(self.images_path, label)
        if not os.path.exists(path):
            os.mkdir (path)



  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)

    ## 4. Capture Images
    k=0

    cv2.imshow("Python zeed capturar imagenes", cv_image)
    if (self.label < int(size(self.labels))):
        k = cv2.waitKey(1)
        if k%256 == 32:
            #Lavel
            label =self.labels[self.label ]
            #Image path
            imgname = os.path.join(self.images_path,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
            cv2.imwrite(imgname, cv_image)
            print('Collecting image {}'.format(self.imgnum))
            self.imgnum = self.imgnum+1
            if (self.imgnum == self.number_imgs ):
                self.imgnum = 0
                self.label =self.label +1
    else:
        cv2.destroyAllWindows()











def main(args):
  ic = image_converter()
  rospy.init_node('image_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")

  cv2.destroyAllWindows()


if __name__ == '__main__':

    main(sys.argv)