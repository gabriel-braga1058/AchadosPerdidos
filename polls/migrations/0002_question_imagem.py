# Generated by Django 4.1.3 on 2023-03-24 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='imagem',
            field=models.ImageField(default='', upload_to='uploads/'),
        ),
    ]
