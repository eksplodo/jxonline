# Generated by Django 2.0.3 on 2018-03-13 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20180312_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseresource',
            name='name',
            field=models.CharField(max_length=100, verbose_name='资源名称'),
        ),
    ]
