# Generated by Django 3.1.2 on 2020-10-06 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0002_auto_20201006_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
