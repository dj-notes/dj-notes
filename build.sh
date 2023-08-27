#!/bin/bash

pip install -r requirements.txt
python3.9 manage.py migrate
mkdir staticfiles/
python3.9 manage.py collectstatic --no-input