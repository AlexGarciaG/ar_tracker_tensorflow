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
	- For easier installation of TensorFlow-Gput Windows is required.
