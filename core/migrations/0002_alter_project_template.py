# Generated by Django 3.2.6 on 2021-08-14 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='template',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]