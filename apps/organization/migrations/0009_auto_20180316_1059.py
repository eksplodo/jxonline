# Generated by Django 2.0.3 on 2018-03-16 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0008_teacher_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(upload_to='teacher/%Y%m', verbose_name='教师头像'),
        ),
    ]