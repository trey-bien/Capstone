# Generated by Django 3.1.2 on 2020-10-05 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('bio', models.TextField()),
                ('photo', models.ImageField(height_field=30, upload_to='uploads/', width_field=15)),
            ],
        ),
    ]
