# Generated by Django 3.2.9 on 2021-12-08 01:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=45)),
                ('nickname', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=45, unique=True)),
                ('github', models.CharField(max_length=200, null=True)),
                ('profile_photo', models.URLField(null=True)),
                ('description', models.TextField(null=True)),
                ('position', models.CharField(max_length=45, null=True)),
                ('subscribe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
