# Generated by Django 2.1.4 on 2018-12-06 09:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20181206_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='views',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество просмотров'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='name',
            field=models.CharField(max_length=500, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='text',
            field=models.TextField(verbose_name='Текст'),
        ),
    ]