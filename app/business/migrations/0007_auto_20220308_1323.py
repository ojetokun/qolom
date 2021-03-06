# Generated by Django 3.1 on 2022-03-08 12:23

import core.common.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0006_auto_20220304_1903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bank',
            old_name='email_confirmation',
            new_name='activated',
        ),
        migrations.RenameField(
            model_name='bank',
            old_name='business',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='user_has_seen_notification',
            new_name='buyer_notified',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='has_been_activated',
            new_name='paid',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='will_be_ready_by',
            new_name='was_ready_by',
        ),
        migrations.RemoveField(
            model_name='bank',
            name='recipient_info',
        ),
        migrations.AddField(
            model_name='order',
            name='seller_notified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(1, 'Awaiting Payment'), (2, 'Sent'), (3, 'Ready'), (4, 'Collected')]),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=core.common.fields.DefaultIntegerField(blank=True, default=0, null=True),
        ),
    ]
