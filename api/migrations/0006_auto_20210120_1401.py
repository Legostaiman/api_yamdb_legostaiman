# Generated by Django 3.0.5 on 2021-01-20 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210120_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='rating',
            field=models.IntegerField(blank=True, null=True, verbose_name='рейтинг'),
        ),
    ]
