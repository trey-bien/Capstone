# Generated by Django 3.1.2 on 2020-10-06 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('director', models.CharField(default=True, max_length=30)),
                ('description', models.TextField()),
                ('date_released', models.CharField(max_length=20)),
                ('instructions', models.TextField()),
                ('photo', models.ImageField(height_field=30, upload_to='uploads/', width_field=15)),
                ('genre', models.TextField()),
                ('actors', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='actors.actor')),
            ],
        ),
    ]
