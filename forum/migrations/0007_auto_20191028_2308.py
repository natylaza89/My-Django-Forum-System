# Generated by Django 2.2.6 on 2019-10-28 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_auto_20191028_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='reply_to_older_reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='forum.Reply'),
        ),
    ]
