#!/bin/bash

cd app
mkdir files
python3 -m venv env
source env/bin/activate
pip install -U -r requirements.txt
python3 app/run.py
