# Generated by Django 5.1.4 on 2025-01-12 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boat',
            name='model',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='boat',
            name='production',
            field=models.CharField(max_length=100),
        ),
    ]
