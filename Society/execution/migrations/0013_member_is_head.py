# Generated by Django 3.2.7 on 2021-09-30 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('execution', '0012_guest_is_delete'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='is_head',
            field=models.BooleanField(default=False),
        ),
    ]
