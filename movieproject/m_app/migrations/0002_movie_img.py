# Generated by Django 4.0.4 on 2022-04-21 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='new', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
