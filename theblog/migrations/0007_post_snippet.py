# Generated by Django 2.2.14 on 2021-05-23 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0006_auto_20210522_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click link above to read blog', max_length=255),
        ),
    ]
