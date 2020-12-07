import telegram
from django.conf import settings
from django.core.mail import send_mail
from xtmovers.settings import EMAIL_HOST_USER
from xtmovers.celery import app

@app.task
def send_message():
    send_mail(
        "Received new quote",
        "Check the admin panel",
        EMAIL_HOST_USER,
        ['aktan.r.a@gmail.com'],
        fail_silently=False,
    )


@app.task
def send_message_tg():
    telegram_settings = settings.TELEGRAM
    bot = telegram.Bot(token=telegram_settings['bot_token'])
    bot.send_message(chat_id=f"@{telegram_settings['channel_name']}", text='Ai delai!')

