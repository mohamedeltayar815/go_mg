# Generated by Django 2.2.13 on 2021-05-02 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20210502_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visit',
            name='lap',
        ),
        migrations.RemoveField(
            model_name='visit',
            name='lap01',
        ),
        migrations.RemoveField(
            model_name='visit',
            name='sonar',
        ),
        migrations.RemoveField(
            model_name='visit',
            name='sonar01',
        ),
        migrations.RemoveField(
            model_name='visit',
            name='sonar02',
        ),
        migrations.RemoveField(
            model_name='visit',
            name='sonar03',
        ),
    ]
