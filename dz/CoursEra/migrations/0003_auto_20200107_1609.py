# Generated by Django 3.0.2 on 2020-01-07 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoursEra', '0002_auto_20200107_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars'),
        ),
    ]
