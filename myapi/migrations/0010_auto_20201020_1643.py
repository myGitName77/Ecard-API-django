# Generated by Django 3.1.2 on 2020-10-20 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0009_auto_20201020_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]