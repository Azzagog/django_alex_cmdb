#!/bin/bash
### temporary init script needs to be rewritten in python
###apply migration
python manage.py makemigrations steplogic &&
python manage.py migrate steplogic &&
echo 'migrations applied'
###collect static
[[ -d static_collect ]] && rm -rf static_collect
python manage.py collectstatic && echo 'static files collected'
###run the server
python manage.py runserver 0.0.0.0:8000