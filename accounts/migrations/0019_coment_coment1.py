# Generated by Django 2.2.13 on 2021-05-14 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_vitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='coment1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coment', models.TextField()),
                ('vI', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.vItem')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='coment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coment', models.TextField()),
                ('mit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.maqal')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
