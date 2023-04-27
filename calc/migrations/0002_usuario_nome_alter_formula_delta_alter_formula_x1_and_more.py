# Generated by Django 4.2 on 2023-04-27 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='nome',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='formula',
            name='delta',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='formula',
            name='x1',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='formula',
            name='x2',
            field=models.IntegerField(null=True),
        ),
    ]