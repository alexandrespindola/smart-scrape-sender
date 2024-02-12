from django import forms
from .models import EmailRecipient, EmailMessagePT, EmailMessageEN, EmailMessageES

class EmailRecipientForm(forms.ModelForm):
    class Meta:
        model = EmailRecipient
        fields = ['email', 'language']

class EmailMessageForm(forms.ModelForm):
    class Meta:
        model = EmailMessagePT  # Aqui você pode escolher a model que deseja usar
        fields = ['subject', 'message', 'recipients']