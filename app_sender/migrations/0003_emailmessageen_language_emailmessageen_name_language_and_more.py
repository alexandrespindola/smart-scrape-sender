# Generated by Django 5.0.2 on 2024-02-12 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_sender', '0002_emailmessageen_category_emailmessagees_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailmessageen',
            name='language',
            field=models.CharField(default='en', max_length=2),
        ),
        migrations.AddField(
            model_name='emailmessageen',
            name='name_language',
            field=models.CharField(default='English', max_length=10),
        ),
        migrations.AddField(
            model_name='emailmessagees',
            name='language',
            field=models.CharField(default='es', max_length=2),
        ),
        migrations.AddField(
            model_name='emailmessagees',
            name='name_language',
            field=models.CharField(default='Español', max_length=10),
        ),
        migrations.AddField(
            model_name='emailmessagept',
            name='language',
            field=models.CharField(default='pt', max_length=2),
        ),
        migrations.AddField(
            model_name='emailmessagept',
            name='name_language',
            field=models.CharField(default='Português', max_length=10),
        ),
    ]
