# Generated by Django 2.0.4 on 2018-05-09 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ojss_app', '0021_subcategory_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='sub_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ojss_app.Subcategory'),
        ),
    ]
