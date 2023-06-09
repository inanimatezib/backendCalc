# Generated by Django 4.2 on 2023-04-27 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0003_remove_formula_input_value1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formula',
            name='delta',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='formula',
            name='res1',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='formula',
            name='res2',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='formula',
            name='x1',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='formula',
            name='x2',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='formula',
            name='x3',
            field=models.FloatField(default=0),
        ),
    ]
