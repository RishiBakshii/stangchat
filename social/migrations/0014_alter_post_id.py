# Generated by Django 3.2.13 on 2022-06-19 08:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0013_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default=uuid.UUID('d6edaf71-b899-41df-8f46-5dbd67064c4c'), primary_key=True, serialize=False),
        ),
    ]
