from django.core.mail import send_mail
from django.core import mail
from django.conf import settings


settings.configure(
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend',
    EMAIL_HOST_USER =
    EMAIL_HOST_PASSWORD =
    EMAIL_HOST =
    EMAIL_PORT =
    EMAIL_USE_TLS = True
)

send_mail('Subject here', 'Here is the message.', 'sender',
    ['recipents'])
