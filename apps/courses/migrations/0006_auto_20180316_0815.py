# Generated by Django 2.0.3 on 2018-03-16 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20180316_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='courses/%Y%m', verbose_name='课程刊图'),
        ),
    ]
