web: newrelic-admin run-program gunicorn time_bot.wsgi --log-file -
beat: celery -A time_bot worker -B -l info
release: python manage.py migrate
