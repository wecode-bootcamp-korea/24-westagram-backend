# Generated by Django 3.2.6 on 2021-08-25 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posting',
            name='posting_user',
        ),
    ]
