from django.contrib import admin
from . models import EmailRecipient, EmailMessagePT, EmailMessageEN, EmailMessageES

admin.site.register(EmailRecipient)
admin.site.register(EmailMessagePT)
admin.site.register(EmailMessageEN)
admin.site.register(EmailMessageES)