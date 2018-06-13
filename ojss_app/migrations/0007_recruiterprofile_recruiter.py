# Generated by Django 2.0.4 on 2018-05-07 12:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ojss_app', '0006_remove_recruiterprofile_company_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruiterprofile',
            name='recruiter',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
