# Generated by Django 2.2.4 on 2020-08-21 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dongsugong', '0012_dsg_subject'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dsg',
            options={'ordering': ['-created_at']},
        ),
    ]
