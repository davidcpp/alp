# Generated by Django 3.0.5 on 2020-04-14 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='place',
        ),
        migrations.AddField(
            model_name='team',
            name='comments',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='match',
            name='comments',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_short',
            field=models.CharField(default='', max_length=10),
        ),
    ]
