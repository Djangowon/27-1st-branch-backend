# Generated by Django 3.2.9 on 2021-12-08 01:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('postings', '0001_initial'),
        ('users', '0001_initial'),
        ('keywords', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostingsPostingTags',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('posting', models.ForeignKey(db_column='posting_id', on_delete=django.db.models.deletion.CASCADE, to='postings.posting')),
            ],
            options={
                'db_table': 'postings_postingtags',
            },
        ),
        migrations.CreateModel(
            name='UsersUserTags',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'users_usertags',
            },
        ),
        migrations.CreateModel(
            name='UserTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=45, unique=True)),
                ('users', models.ManyToManyField(related_name='user_tags', through='branch_tags.UsersUserTags', to='users.User')),
            ],
            options={
                'db_table': 'user_tags',
            },
        ),
        migrations.AddField(
            model_name='usersusertags',
            name='user_tag',
            field=models.ForeignKey(db_column='user_tag_id', on_delete=django.db.models.deletion.CASCADE, to='branch_tags.usertag'),
        ),
        migrations.CreateModel(
            name='PostingTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=45, unique=True)),
                ('keyword', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='keywords.keyword')),
                ('postings', models.ManyToManyField(related_name='posting_tags', through='branch_tags.PostingsPostingTags', to='postings.Posting')),
            ],
            options={
                'db_table': 'posting_tags',
            },
        ),
        migrations.AddField(
            model_name='postingspostingtags',
            name='posting_tag',
            field=models.ForeignKey(db_column='posting_tag_id', on_delete=django.db.models.deletion.CASCADE, to='branch_tags.postingtag'),
        ),
    ]
