# Generated by Django 2.0.4 on 2018-05-09 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ojss_app', '0026_auto_20180509_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message_type',
            field=models.CharField(max_length=1),
        ),
    ]
