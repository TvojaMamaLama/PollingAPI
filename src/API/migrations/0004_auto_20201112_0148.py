# Generated by Django 3.1.3 on 2020-11-11 22:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_auto_20201112_0045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='name',
        ),
        migrations.AddField(
            model_name='choice',
            name='right',
            field=models.BooleanField(default=False, verbose_name='Правильность ответа'),
        ),
        migrations.AddField(
            model_name='question',
            name='description',
            field=models.CharField(default=1, max_length=500, verbose_name='Описание вопроса'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='poll',
            name='begin_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Начало опроса'),
        ),
        migrations.AlterField(
            model_name='poll',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 12, 2, 48, 20, 653550, tzinfo=utc), verbose_name='Конец опроса'),
        ),
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('TXT', 'Текстовый'), ('ONE', 'Один вариант'), ('MUL', 'Несколько вариантов')], max_length=3, verbose_name='Тип вопроса'),
        ),
    ]
