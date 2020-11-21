from django.core.mail import EmailMultiAlternatives
from threading import Thread
from django.core.mail import message
from django.shortcuts import render
from django.template.loader import render_to_string
from django.conf import settings


def send_async_email(message):
    message.send()


def send_email(subject, to, data):
    content_html = render_to_string('mail/account_information.html', {'new_user': data})
    content_txt = render_to_string('mail/account_information.txt', {'new_user': data})

    message = EmailMultiAlternatives(subject, content_txt, settings.EMAIL_HOST_USER, [to])
    message.attach_alternative(content_html, "text/html")

    thread = Thread(target=send_async_email, args=[message])
    thread.start()

    return thread
