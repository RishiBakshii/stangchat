# Generated by Django 3.2.13 on 2022-06-19 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0025_alter_message_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.CharField(blank=True, default='2022/06/19 08:35:20', max_length=1000000),
        ),
    ]
