# Generated by Django 5.1.4 on 2025-01-12 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('production', models.IntegerField()),
                ('image', models.ImageField(default='', upload_to='main_app/static/uploads/')),
            ],
        ),
    ]
