# Generated by Django 4.1.5 on 2023-01-13 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mriic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]