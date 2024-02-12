#!/bin/bash
python manage.py compilescss
python manage.py collectstatic --noinput
pkill -f runserver
python manage.py runserver