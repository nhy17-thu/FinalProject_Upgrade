# Generated by Django 2.2.4 on 2019-09-13 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190911_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='pic',
            name='faces',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
