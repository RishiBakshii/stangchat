# Generated by Django 3.2.13 on 2022-06-16 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_profile_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('stangmessage', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='no_of_likes',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
