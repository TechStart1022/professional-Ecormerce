# Generated by Django 4.2.9 on 2024-02-17 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_review_productfaq'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('rate', models.IntegerField(default=0, help_text='Numbers added here are in pecentage e.g 5 %')),
                ('active', models.BooleanField(default=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Taxes',
                'ordering': ['country'],
            },
        ),
    ]
