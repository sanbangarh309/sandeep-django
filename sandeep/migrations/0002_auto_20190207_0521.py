# Generated by Django 2.1.5 on 2019-02-07 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sandeep', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FileField(upload_to='sandeep/static/img/projects/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.FileField(upload_to='sandeep/static/img/profile/'),
        ),
    ]
