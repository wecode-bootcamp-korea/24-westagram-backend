# Generated by Django 3.2.6 on 2021-08-25 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postings', '0003_auto_20210825_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postingcomment',
            name='comment_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
