# Generated by Django 4.2.9 on 2024-02-16 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0005_remove_user_uidb'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='full_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
