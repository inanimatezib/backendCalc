# Generated by Django 4.2 on 2023-04-27 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_value1', models.IntegerField()),
                ('input_value2', models.IntegerField()),
                ('input_value3', models.IntegerField()),
                ('delta', models.IntegerField()),
                ('x1', models.IntegerField()),
                ('x2', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
