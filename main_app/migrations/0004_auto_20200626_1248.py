# Generated by Django 3.0.7 on 2020-06-26 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20200626_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.CharField(max_length=200),
        ),
    ]
