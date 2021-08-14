# Generated by Django 3.2.6 on 2021-08-14 01:11

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='About me', max_length=200)),
                ('overview', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('overview', tinymce.models.HTMLField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('thumbnail', models.FileField(upload_to='images')),
                ('django', models.BooleanField(blank=True, default=False)),
                ('sqlite', models.BooleanField(blank=True, default=False)),
                ('golang', models.BooleanField(blank=True, default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Cv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='cv', max_length=100)),
                ('cv', models.FileField(upload_to='cv')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='cv', max_length=100)),
                ('picture', models.FileField(default='Profile_pics', upload_to='profile')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overview', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('thumbnail', models.FileField(upload_to='images')),
                ('django', models.BooleanField(blank=True, default=False)),
                ('sqlite', models.BooleanField(blank=True, default=False)),
                ('golang', models.BooleanField(blank=True, default=False)),
                ('featured', models.BooleanField(blank=True, default=False)),
                ('url', models.CharField(max_length=500)),
                ('template', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='core.article')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]