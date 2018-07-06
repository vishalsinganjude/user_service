#!/bin/bash
python user_service/manage.py makemigrations
python user_service/manage.py migrate
