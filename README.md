# ar_tracker_tensorflow
## Introduction
### Objective
The purpose of this project is to analyze the possibility of using TensorFlow as an ar tag tracker, so it can be used as a sensor for an autonomous navigation rover.
This project is relevant, because even if there are technologies that can perform this task, they can’t be used in low end computers neither be trained to identify new ar tags. 
### Project requirements 
- The project must be able to recognize the followings ar tags provide by ROS package [ar_track_alvar](http://wiki.ros.org/ar_track_alvar)
![ar tags]( http://wiki.ros.org/ar_track_alvar?action=AttachFile&do=get&target=markers0to8.png)

- Must be compatible with the technologies used by the team EagleX Robotics so it can be used in an autonomous navigation rover.
    - [Ubuntu](https://ubuntu.com/download/desktop)
    - [ROS Noetic](http://wiki.ros.org/noetic)
    - Python/C
- Must be able to be executed in a Raspberry pi 4 8 Gb RAM
- Must have the following performance
    - Low latency
    - Hight Precision
    - Low Recall is acceptable
## Installation 
### Requirements 
#### Hardware
- Raspberry pi 4 8 Gb RAM
- Computer for train the model, preference with Nvidia Graphics for TensorFlow -Gpu training.
#### Software
- Raspberry pi 4 8 Gb RAM
    - [Ubuntu mate 20.04 64bits]( https://ubuntu-mate.org/download/arm64/focal/thanks/?method=direct)
    - [ROS Noetic](http://wiki.ros.org/noetic)
- Computer for train the model
    - For easier installation of TensorFlow-Gpu Windows is required.
### TensorFlow Installation
#### Computer for train and testing the model
1. Clone the repository:
```
git clone https://github.com/AlexGarciaG/ar_tracker_tensorflow.git
```
2. Use the jupyther notebook in *src\BasicTensorFlow\Instalation\2. Install tensorflow.ipynb*.  
**Note: For this step is recommendable to follow the tutorial used for this project [Tensorflow Object Detection in 5 Hours with Python | Full Course with 3 Projects](https://www.youtube.com/watch?v=yqkISICHH-U) and  install tensorflow-gpu instead of  tensorflow  if you want to traing unsing Gpu, this is because tensorflow  and tensorflow-gpu  can not be installed at the same time**
### Train models 
#### Train models 
1. Collect Images and lavel then using the jupyther notebook *\src\BasicTensorFlow\ImageColleting\1. Image Collection.ipynb*  
2. Chose a pre trained model of [ThensorFlow models zoo]( https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md)
3. Copy the folder *src\BasicTensorFlow\Template* and changes its name to the chosen model
4. Open the jupyther notebook *1. Training and Detection.ipynb* in your new folder
5. Copy the link from the model chosen from [ThensorFlow models zoo]( https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md) to the global variable PRETRAINED_MODEL_URL  in the jupyther notebook
Example 
“””
PRETRAINED_MODEL_URL = 'http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8.tar.gz'
“””
6. Copy the link from the model chosen from [ThensorFlow models zoo]( https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md) in a browser and copy the name of the file that wants to be downloaded to variable PRETRAINED_MODEL_NAME in the jupyther notebook
Example 
“””
PRETRAINED_MODEL_NAME = 'ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8'
“””
7. In the model folder copy the training images and its level used in *Tensorflow\workspace\images \train*  
8. In the model folder copy the training images and its level used in *Tensorflow\workspace\images \test*  
9. In section 2 of the jupyther notebook *1. Training and Detection.ipynb*, change the labels names fot the ones used when the images were label
“””
 labels = [{'name':'ar1', 'id':1}, {'name':'ar2', 'id':2}, {'name':'ar3', 'id':3}, {'name':'ar4', 'id':4}]
“””
10. Execute until the first line of section 6 of the jupyther notebook *1. Training and Detection.ipynb* 
11. Execute in a terminal the output given in the first line of section 6 of the jupyther notebook *1. Training and Detection.ipynb*  
**Note: This command will start the training and by default training steps are 10000, but it can be changed to higher number when the full model is trained. The variable to modify in the command is --num_train_steps=10000 **
10. Execute until the first line of section 7 of the jupyther notebook *1. Training and Detection.ipynb* 
11. Execute in a terminal the output given in the first line of section 7 of the jupyther notebook *1. Training and Detection.ipynb*  
**Note: This command will start the testing it could takes more time than the training because it is waiting for more data**
#### Check the trained models
1.  Open *\Tensorflow\workspace\models\my_ssd_mobnet* of your folder model in a terminal
2. 
- To see the training process, open the folder /train
- To see the test results, open the folder /eval
3. Execute the following command 
“””
tensorboard --logdir=.
“””
4. In a browser open the following link http://localhost:6006/#scalars 
### Open a trained model
1. Open * 2. Execute model on wedcam * of your folder model in a terminal
2. Execute all the lines, it will open a window where the ar tag detections is make. 
**Note: Use q to close the windows**

 
## Issues
- [x] Install Cuda in Ubuntu
- [ ] Install a compatible  TensorFlow-Gpy in Ubuntu
- [x] Low memory computer
 	- Acquire more memory RAM
- [ ] Make TensorFlow use Gpu
## Project status
- [x] Install TensorFlow-Gpu for training model
- [x] Compile 20 images for 4 ar tags
- [x] Train the model used in the [tutorial](https://www.youtube.com/watch?v=yqkISICHH-U)
- [x] Test the trained model in the computer used for train the model
- [x] Train different model using [pre trained models of TensorFlow]( https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md)
- [ ] Export trained models and test in raspberry pi 4 8Gb Ram 
- [ ] Adapt the trained models so they are compatible with ROS Noetic
- [ ] Compile 100 images or each ar tag, in brighter environment with different angles and distances.
- [ ]  Train the models with the new data set
- [ ] Test the new trained models.


