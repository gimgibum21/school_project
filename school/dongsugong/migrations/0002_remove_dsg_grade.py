# Generated by Django 2.2.4 on 2020-08-18 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dongsugong', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dsg',
            name='grade',
        ),
    ]