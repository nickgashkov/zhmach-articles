# Generated by Django 2.1.4 on 2018-12-07 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20181206_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d/', verbose_name='Изображение'),
        ),
    ]