# Generated by Django 3.1 on 2020-08-13 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='updated_at',
        ),
    ]