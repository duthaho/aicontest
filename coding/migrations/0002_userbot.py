# Generated by Django 4.2 on 2023-06-27 04:45

import coding.models.bot
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import hashid_field.field


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coding', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBot',
            fields=[
                ('id', hashid_field.field.HashidAutoField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', min_length=7, prefix='', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('activate', models.BooleanField(default=False)),
                ('url', models.FileField(upload_to=coding.models.bot.user_bot_path)),
                ('win', models.PositiveIntegerField(default=0)),
                ('draw', models.PositiveIntegerField(default=0)),
                ('lose', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bots', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'coding_userbot',
            },
        ),
    ]
