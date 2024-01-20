#!/bin/bash

JSON_STRING='{"name": "Admin", "email": "'$1'", "password": "'$2'"}'

echo "$JSON_STRING" > admin_data.json

python main.py
