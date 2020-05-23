# Generated by Django 3.0.5 on 2020-05-23 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alp', '0019_auto_20200523_1208'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='league',
            options={'ordering': ['league_name']},
        ),
        migrations.RemoveField(
            model_name='league',
            name='season',
        ),
        migrations.AlterField(
            model_name='league',
            name='league_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='round_game',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='sport',
            name='sport_name',
            field=models.CharField(default='Football', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_short',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
