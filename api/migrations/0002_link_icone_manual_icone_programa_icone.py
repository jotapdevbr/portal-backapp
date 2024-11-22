# Generated by Django 5.1 on 2024-11-12 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='icone',
            field=models.ImageField(blank=True, upload_to='icones/'),
        ),
        migrations.AddField(
            model_name='manual',
            name='icone',
            field=models.ImageField(blank=True, upload_to='icones/'),
        ),
        migrations.AddField(
            model_name='programa',
            name='icone',
            field=models.ImageField(blank=True, upload_to='icones/'),
        ),
    ]
