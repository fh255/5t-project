# Generated by Django 3.2.4 on 2024-08-08 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default_profile.png', upload_to='images/'),
        ),
    ]
