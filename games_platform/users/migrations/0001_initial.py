# Generated by Django 4.0.3 on 2022-03-20 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=255, unique=True, verbose_name='username')),
                ('role', models.CharField(choices=[('GAMER', 'GAMER'), ('DEVELOPER', 'DEVELOPER'), ('ADMIN', 'ADMIN'), ('DEVELOPER', 'DEVELOPER')], max_length=30, verbose_name='role')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last_login')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
