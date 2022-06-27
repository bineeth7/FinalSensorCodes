# Generated by Django 4.0.5 on 2022-06-27 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rainfall', models.FloatField(max_length=30)),
                ('vibration', models.FloatField(max_length=3)),
                ('moisture', models.FloatField(max_length=5)),
                ('status', models.IntegerField()),
            ],
        ),
    ]