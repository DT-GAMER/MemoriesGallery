# Generated by Django 3.1.7 on 2023-08-25 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multimedia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='memory',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='memories/videos/'),
        ),
    ]
