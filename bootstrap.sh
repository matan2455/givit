#!/usr/bin/env bash
echo "install python and pip3"
apt update
apt install -y python3.7 python3-pip
pip3 install --upgrade pip
pip3 install django==3.1