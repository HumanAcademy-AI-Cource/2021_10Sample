#!/bin/bash

sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys F42ED6FBAB17C654
sudo apt update
sudo apt install -y ros-melodic-rqt ros-melodic-rqt-common-plugins python-pyqtgraph ros-melodic-rosbridge-server python-pyaudio
