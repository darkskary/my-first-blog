# Generated by Django 2.0.13 on 2019-03-17 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='specifications',
            field=models.ImageField(null=True, upload_to='imagen_specifications'),
        ),
    ]
