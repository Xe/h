#!/bin/bash

virtualenv env
. ./env/bin/activate

pip install git+https://github.com/billpmurphy/hask
pip install -r requirements.txt 
