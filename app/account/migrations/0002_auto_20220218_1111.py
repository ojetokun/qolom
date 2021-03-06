# Generated by Django 3.1 on 2022-02-18 10:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('business', '0001_initial'),
        ('users', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='current_business_queue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='people_on_queue', to='business.businessqueue'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='current_user_queue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='people_on_queue', to='users.userqueue'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='favourites',
            field=models.ManyToManyField(related_name='favourites', to='account.BusinessProfile'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='userProfile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usercalendar',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='calendar', to='account.userprofile'),
        ),
        migrations.AddField(
            model_name='calendar',
            name='business',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='calendar', to='account.businessprofile'),
        ),
        migrations.AddField(
            model_name='businessprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='business', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddIndex(
            model_name='businessprofile',
            index=models.Index(fields=['name', 'address', 'state'], name='account_bus_name_d94d8e_idx'),
        ),
    ]
