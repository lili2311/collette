web: python collette/manage.py collectstatic --noinput; bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT collette/settings.py
web: gunicorn collette.wsgi --log-file -
