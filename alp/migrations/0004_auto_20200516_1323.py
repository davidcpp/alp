# Generated by Django 3.0.5 on 2020-05-16 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alp', '0003_auto_20200516_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='comments',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='comments',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_name',
            field=models.CharField(max_length=100),
        ),
    ]
