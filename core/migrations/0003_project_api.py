# Generated by Django 3.2.6 on 2021-08-31 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_project_template'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='api',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]