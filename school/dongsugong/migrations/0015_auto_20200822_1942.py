# Generated by Django 2.2.4 on 2020-08-22 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dongsugong', '0014_dsg_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dsg',
            name='content',
            field=models.TextField(verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='dsg',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='게시일'),
        ),
        migrations.AlterField(
            model_name='dsg',
            name='grade',
            field=models.CharField(default='1학년', max_length=20, verbose_name='학년'),
        ),
        migrations.AlterField(
            model_name='dsg',
            name='image',
            field=models.ImageField(blank=True, upload_to='dongsugong/img', verbose_name='사진'),
        ),
        migrations.AlterField(
            model_name='dsg',
            name='subject',
            field=models.CharField(default='', max_length=20, verbose_name='과목'),
        ),
        migrations.AlterField(
            model_name='dsg',
            name='title',
            field=models.CharField(max_length=200, verbose_name='제목'),
        ),
        migrations.AlterField(
            model_name='dsg',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='수정일'),
        ),
    ]
