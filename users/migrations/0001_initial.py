# Generated by Django 3.1 on 2022-02-09 16:56

import core.common.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0003_auto_20220209_1756'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserQueue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('activated_at', models.DateTimeField(blank=True, null=True)),
                ('deactivated_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', core.common.fields.DefaultCharField(blank=True, max_length=255, null=True)),
                ('instruction', core.common.fields.DefaultCharField(blank=True, max_length=255, null=True)),
                ('information', core.common.fields.DefaultCharField(blank=True, max_length=255, null=True)),
                ('key', models.CharField(blank=True, max_length=8, null=True, unique=True)),
                ('slug', models.SlugField(db_index=False, max_length=80)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='owned_user_queue', to='account.userprofile')),
            ],
            options={
                'verbose_name': '[ User Queue ]',
                'ordering': ['-created_at'],
            },
        ),
    ]
