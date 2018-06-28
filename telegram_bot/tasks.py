import requests
from celery import task
from celery.utils.log import get_task_logger
from django.conf import settings
from datetime import datetime


logger = get_task_logger(__name__)

@task
def send_message_to_telegram_task():
    chat_id = settings.TELEGRAM_CHAT_ID
    token = settings.TELEGRAM_NOTIFICATIONS_TOKEN
    message = datetime.now().time().strftime("%H:%M")
    url = "https://api.telegram.org/bot{}/sendMessage".format(token)
    r = requests.post(url, data={'chat_id': chat_id, 'text': message})
    r.raise_for_status()
    logger.info('Sent message to telegram: {}'.format(message))


@task
def check_app_task():
    logger.info('Start')
    logger.info('End')
