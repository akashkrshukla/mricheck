# Generated by Django 3.0.3 on 2020-08-16 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagescans', '0003_auto_20200816_0545'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagescans',
            name='analyzed_image',
            field=models.FileField(blank=True, null=True, upload_to='ImageResults'),
        ),
    ]
