# Generated by Django 3.2.7 on 2022-01-18 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20220119_0012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='thumbnail',
        ),
    ]
