# Generated by Django 3.1 on 2022-03-10 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20220308_1323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cardinformation',
            old_name='card_bin',
            new_name='bin',
        ),
    ]
