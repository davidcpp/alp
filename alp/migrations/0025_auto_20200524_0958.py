# Generated by Django 3.0.5 on 2020-05-24 07:58

from django.db import migrations
import django.db.models.functions.text


class Migration(migrations.Migration):

    dependencies = [
        ('alp', '0024_auto_20200523_2326'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': [django.db.models.functions.text.Upper('team_name')]},
        ),
    ]
