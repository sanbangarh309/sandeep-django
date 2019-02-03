# Generated by Django 2.1.5 on 2019-02-03 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sandeep', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FileField(upload_to='static/img/projects/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='when',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date created'),
        ),
    ]
