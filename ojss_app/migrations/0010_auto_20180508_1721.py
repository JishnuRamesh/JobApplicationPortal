# Generated by Django 2.0.4 on 2018-05-08 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ojss_app', '0009_auto_20180508_0853'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_letter', models.CharField(max_length=1000)),
                ('cv', models.CharField(max_length=1000)),
                ('matching_score', models.IntegerField()),
                ('status', models.CharField(choices=[('A', 'ACTIVE'), ('S', 'SELECTED'), ('R', 'REJECTED')], default='M', max_length=1)),
            ],
        ),
        migrations.AlterField(
            model_name='job',
            name='job_description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AddField(
            model_name='application',
            name='job_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ojss_app.Job'),
        ),
        migrations.AddField(
            model_name='application',
            name='seeker_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ojss_app.SeekerProfile'),
        ),
    ]
