#!/bin/bash
apt update -y
apt install python3 -y
apt install python3-pip -y

apt-get install libmysqlclient-dev -y


mkdir -p ~/.local/bin
touch ~/.bashrc
echo 'PATH=$PATH:~/.local/bin' > ~/.bashrc

sudo chown -R $(whoami):$(whoami) ~/*
source ~/.bashrc

pip install --user ansible

ansible --version