# Generated by Django 2.0.5 on 2018-07-18 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userstories', '0006_auto_20180716_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupy',
            name='group_name',
            field=models.CharField(default='podstawowa', max_length=64, verbose_name='Nazwa grupy'),
        ),
    ]
