# Generated by Django 3.2.6 on 2021-08-25 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='post_time',
            field=models.DateField(auto_now_add=True),
        ),
    ]