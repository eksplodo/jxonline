# Generated by Django 2.0.3 on 2018-03-12 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20180312_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='name',
            field=models.CharField(default='', max_length=20, verbose_name='机构名称'),
            preserve_default=False,
        ),
    ]
