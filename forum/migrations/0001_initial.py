# Generated by Django 2.2.6 on 2019-11-14 16:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_body', models.TextField(default='')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('announcement', models.CharField(choices=[('normal', 'normal'), ('pinned', 'pinned')], default='normal', max_length=12)),
                ('author', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('moderator', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MainTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_body', models.TextField(default='')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('announcement', models.CharField(choices=[('normal', 'normal'), ('pinned', 'pinned')], default='normal', max_length=12)),
                ('title', models.CharField(default='', max_length=50)),
                ('closed', models.BooleanField(default=False)),
                ('author', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('forum', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.Forum')),
                ('like_list', models.ManyToManyField(blank=True, related_name='_maintopic_like_list_+', to=settings.AUTH_USER_MODEL)),
                ('unlike_list', models.ManyToManyField(blank=True, related_name='_maintopic_unlike_list_+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_body', models.TextField(default='')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('announcement', models.CharField(choices=[('normal', 'normal'), ('pinned', 'pinned')], default='normal', max_length=12)),
                ('author', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('forum', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.Forum')),
                ('like_list', models.ManyToManyField(blank=True, related_name='_reply_like_list_+', to=settings.AUTH_USER_MODEL)),
                ('reply_to_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='forum.Comment')),
                ('reply_to_main_thread', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='forum.MainTopic')),
                ('reply_to_older_reply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.Reply')),
                ('thread_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='forum.MainTopic')),
                ('unlike_list', models.ManyToManyField(blank=True, related_name='_reply_unlike_list_+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ForumCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('forums', models.ManyToManyField(blank=True, to='forum.Forum')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='forum',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.Forum'),
        ),
        migrations.AddField(
            model_name='comment',
            name='like_list',
            field=models.ManyToManyField(blank=True, related_name='_comment_like_list_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='thread_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='forum.MainTopic'),
        ),
        migrations.AddField(
            model_name='comment',
            name='unlike_list',
            field=models.ManyToManyField(blank=True, related_name='_comment_unlike_list_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
