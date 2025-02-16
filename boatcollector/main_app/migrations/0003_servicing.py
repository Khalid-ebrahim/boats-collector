# Generated by Django 5.1.4 on 2025-01-14 10:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_boat_model_alter_boat_production'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('checks', models.CharField(choices=[('one', 'CheckOne'), ('two', 'CheckTwo'), ('three', 'CheckThree')], default='one', max_length=6)),
                ('boat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.boat')),
            ],
        ),
    ]
