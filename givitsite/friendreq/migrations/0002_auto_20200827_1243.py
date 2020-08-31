# Generated by Django 3.1 on 2020-08-27 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friendreq', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemrequest',
            name='friend_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='itemrequest',
            name='isOpen',
            field=models.BooleanField(default=True),
        ),
    ]
