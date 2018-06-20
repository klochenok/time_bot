web: python manage.py collectstatic --noinput; gunicorn time_bot.wsgi --log-file -
beat: celery -A time_bot worker -B -l info
release: python manage.py migrate
