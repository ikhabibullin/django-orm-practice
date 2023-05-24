#!/bin/bash

poetry install
poetry shell

cd src

python manage.py migrate
python manage.py fill_db
