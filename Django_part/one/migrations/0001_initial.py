# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GUID', models.CharField(max_length=36)),
                ('tournament', models.CharField(max_length=100)),
                ('time', models.DateTimeField(max_length=30)),
                ('players', models.CharField(max_length=200)),
                ('coeff', models.CharField(max_length=20)),
                ('result', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GUID', models.CharField(max_length=36)),
                ('name', models.CharField(max_length=100)),
                ('total_games', models.CharField(max_length=3)),
                ('win_rate', models.CharField(max_length=7)),
                ('svoi_podachi', models.CharField(max_length=9)),
                ('chuz_podachi', models.CharField(max_length=9)),
                ('set_rate', models.CharField(max_length=7)),
                ('game_rate', models.CharField(max_length=7)),
                ('break_point', models.CharField(max_length=9)),
            ],
        ),
    ]
