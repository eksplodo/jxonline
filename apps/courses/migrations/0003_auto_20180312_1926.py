# Generated by Django 2.0.3 on 2018-03-12 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20180312_1743'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseresource',
            old_name='coures',
            new_name='course',
        ),
        migrations.AlterField(
            model_name='course',
            name='degree',
            field=models.CharField(choices=[('cj', '初级'), ('zj', '中级'), ('gj', '高级')], max_length=2, verbose_name='等级'),
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(upload_to='courses/%Y%m', verbose_name='课程刊图'),
        ),
    ]