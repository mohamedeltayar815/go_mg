# Generated by Django 2.2.13 on 2021-05-14 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20210514_0802'),
    ]

    operations = [
        migrations.AddField(
            model_name='maqal',
            name='pic',
            field=models.ImageField(blank=True, default='1234.jpg', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='maqal',
            name='pic2',
            field=models.ImageField(blank=True, default='1234.jpg', null=True, upload_to=''),
        ),
    ]