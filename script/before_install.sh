#!/bin/bash
sudo apt update -y
sudo apt install python3 -y
sudo apt install python3-pip -y

sudo apt-get install libmysqlclient-dev -y


sudo mkdir -p ~/.local/bin
sudo touch ~/.bashrc
echo 'PATH=$PATH:~/.local/bin' > ~/.bashrc

sudo chown -R $(whoami):$(whoami) ~/*
source ~/.bashrc

pip3 install --user ansible

ansible --version