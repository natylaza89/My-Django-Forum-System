# Generated by Django 2.2.6 on 2019-10-28 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_auto_20191028_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='reply_to_older_reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.Reply'),
        ),
    ]
