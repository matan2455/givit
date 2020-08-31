#!/usr/bin/env bash

# Installing packages
apt update
apt install -y python3.7 python3-pip postgresql postgresql-contrib
sudo apt install libpq-dev
pip3 install --upgrade pip
pip3 install -r /vagrant/requirements.txt

# DB creation
sudo -u postgres createdb givit
sudo -u postgres psql -c "ALTER ROLE postgres WITH PASSWORD 'givit';"
