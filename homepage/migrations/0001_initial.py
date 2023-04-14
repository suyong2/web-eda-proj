# Generated by Django 4.2 on 2023-04-12 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('price', models.IntegerField(default=0)),
                ('is_ice', models.BooleanField(default=False)),
            ],
        ),
    ]
