#!/bin/bash

# Install Docker
sudo apt update
sudo apt install docker.io -y

#cloning a kali-docker
#sudo git clone https://github.com/srikanthreddy-lectures/v-lab-kali.git
#cd ./v-lab-kali/

#sudo docker build -t mykali .
#sudo docker run --rm -it -d -p 8080:8080 -p 5900:5900 mykali

sudo apt install tightvncserver
tightvncserver -geometry 1024x786

git clone https://github.com/novnc/noVNC.git

cd noVNC
./utils/novnc_proxy --vnc localhost:5901 --listen 0.0.0.0:8080


#sudo docker pull tleemcjr/metasploitable2
#sudo docker run --rm -it -d tleemcjr/metasploitable2:latest