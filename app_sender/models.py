from django.db import models

class EmailRecipient(models.Model):
    LANGUAGES = [
        ('en', 'English'),
        ('es', 'Español'),
        ('pt', 'Português'),
        ('it', 'Italiano'),
        ('de', 'Deutsch'),
    ]
    email = models.EmailField(unique=True)
    language = models.CharField(max_length=2, choices=LANGUAGES, default='en')

    class Meta:
        verbose_name = 'Endereço de E-mail'
        verbose_name_plural = 'Endereços de E-mail'

    def __str__(self):
        return self.email

class EmailMessagePT(models.Model):
    language = models.CharField(max_length=2, default='pt')
    name_language = models.CharField(max_length=10, default='Português')
    category = models.CharField(max_length=200, default='null')
    subject = models.CharField(max_length=200)
    message = models.TextField()
    recipients = models.ManyToManyField(EmailRecipient)
    sent_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'E-mail PORTUGUÊS'
        verbose_name_plural = 'E-mails PORTUGUÊS'

    def __str__(self):
        return self.name_language
    
class EmailMessageEN(models.Model):
    language = models.CharField(max_length=2, default='en')
    name_language = models.CharField(max_length=10, default='English')
    category = models.CharField(max_length=200, default='null')
    subject = models.CharField(max_length=200)
    message = models.TextField()
    recipients = models.ManyToManyField(EmailRecipient)
    sent_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'E-mail ENGLISH'
        verbose_name_plural = 'E-mailS ENGLISH'
    
    def __str__(self):
        return self.name_language
    
class EmailMessageES(models.Model):
    language = models.CharField(max_length=2, default='es')
    name_language = models.CharField(max_length=10, default='Español')
    category = models.CharField(max_length=200, default='null')
    subject = models.CharField(max_length=200)
    message = models.TextField()
    recipients = models.ManyToManyField(EmailRecipient)
    sent_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'E-mail ESPAÑOL'
        verbose_name_plural = 'E-mails ESPAÑOL'
    
    def __str__(self):
        return self.name_language
