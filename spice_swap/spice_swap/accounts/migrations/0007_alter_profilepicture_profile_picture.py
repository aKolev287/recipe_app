# Generated by Django 4.2.4 on 2023-08-17 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_profilepicture_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilepicture',
            name='profile_picture',
            field=models.ImageField(blank=True, default='./profile_pictures/default-pfp.jpg', null=True, upload_to='./profile_pictures/'),
        ),
    ]