# Generated by Django 2.2.4 on 2020-08-20 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dongsugong', '0011_dsg_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='dsg',
            name='subject',
            field=models.CharField(default='', max_length=20),
        ),
    ]
