# Generated by Django 4.2.9 on 2024-02-15 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0004_user_uidb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='uidb',
        ),
    ]
