# Generated by Django 4.2.9 on 2024-02-15 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0002_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='otp',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
