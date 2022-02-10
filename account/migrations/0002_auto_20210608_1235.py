# Generated by Django 3.1 on 2021-06-08 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=251, null=True)),
                ('price', models.IntegerField()),
                ('units_available', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=1000)),
                ('items', models.CharField(max_length=10485760)),
                ('total', models.CharField(max_length=250)),
                ('status', models.CharField(max_length=250)),
                ('pin', models.IntegerField()),
                ('is_active', models.BooleanField(default=False)),
                ('order_status', models.CharField(max_length=250, null=True)),
                ('created', models.DateTimeField()),
                ('ready_time', models.DateTimeField()),
                ('has_seen_notification', models.BooleanField(default=False)),
                ('fees', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Special_line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('instruction', models.CharField(max_length=250, null=True)),
                ('information', models.CharField(max_length=250, null=True)),
                ('uniquefield', models.CharField(blank=True, max_length=8, null=True, unique=True)),
                ('slug', models.SlugField(db_index=False, max_length=80)),
                ('days_open', models.CharField(blank=True, max_length=42, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('mo_o', models.TimeField(blank=True, null=True)),
                ('mo_c', models.TimeField(blank=True, null=True)),
                ('tu_o', models.TimeField(blank=True, null=True)),
                ('tu_c', models.TimeField(blank=True, null=True)),
                ('we_o', models.TimeField(blank=True, null=True)),
                ('we_c', models.TimeField(blank=True, null=True)),
                ('th_o', models.TimeField(blank=True, null=True)),
                ('th_c', models.TimeField(blank=True, null=True)),
                ('fr_o', models.TimeField(blank=True, null=True)),
                ('fr_c', models.TimeField(blank=True, null=True)),
                ('sa_o', models.TimeField(blank=True, null=True)),
                ('sa_c', models.TimeField(blank=True, null=True)),
                ('su_o', models.TimeField(blank=True, null=True)),
                ('su_c', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='business_line',
            name='closeday',
        ),
        migrations.RemoveField(
            model_name='business_line',
            name='closetime',
        ),
        migrations.RemoveField(
            model_name='business_line',
            name='description',
        ),
        migrations.RemoveField(
            model_name='business_line',
            name='offset',
        ),
        migrations.RemoveField(
            model_name='business_line',
            name='openday',
        ),
        migrations.RemoveField(
            model_name='business_line',
            name='opentime',
        ),
        migrations.RemoveField(
            model_name='business_signup',
            name='email',
        ),
        migrations.RemoveField(
            model_name='business_signup',
            name='password',
        ),
        migrations.RemoveField(
            model_name='business_signup',
            name='username',
        ),
        migrations.RemoveField(
            model_name='user_signup',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user_signup',
            name='password',
        ),
        migrations.RemoveField(
            model_name='user_signup',
            name='username',
        ),
        migrations.AddField(
            model_name='business_line',
            name='information',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='business_line',
            name='instruction',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='business_signup',
            name='account_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='business_signup',
            name='bank',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='business_signup',
            name='bank_account_name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='business_signup',
            name='bank_email_confirmation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='business_signup',
            name='days_open',
            field=models.CharField(blank=True, max_length=42, null=True),
        ),
        migrations.AddField(
            model_name='business_signup',
            name='dp',
            field=models.ImageField(null=True, upload_to='profile'),
        ),
        migrations.AddField(
            model_name='business_signup',
            name='fr_c',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='business_signup',
            name='fr_o',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='business_signup',
            name='has_orders',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='business_signup',
            name='key',
            field=models.CharField(blank=True, max_length=7, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='business_signup',
            name='min_age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='business_signup',
            name='mo_c',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='business_signup',
            name='mo_o',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='business_signup',
            name='order_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='business_signup',
            name='recipient_info',
            field=models.CharField(blank=True, max_length=100000, null=True),
        ),
        migrations.AddField(
            model_name='business_signup',
            name='sa_c',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='business_signup',
            name='sa_o',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='business_signup',
            name='su_c',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='business_signup',
            name='su_o',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='business_signup',
            name='th_c',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='business_signup',
            name='th_o',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='business_signup',
            name='timezone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='business_signup',
            name='total_earned',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='business_signup',
            name='total_received',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='business_signup',
            name='tu_c',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='business_signup',
            name='tu_o',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='business_signup',
            name='we_c',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='business_signup',
            name='we_o',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user_signup',
            name='age',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user_signup',
            name='card_information',
            field=models.CharField(default='[]', max_length=1000000, null=True),
        ),
        migrations.AddField(
            model_name='user_signup',
            name='favourites',
            field=models.ManyToManyField(related_name='favourites', to='account.Business_signup'),
        ),
        migrations.AddField(
            model_name='user_signup',
            name='timezone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user_signup',
            name='total_seconds',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user_signup',
            name='unique',
            field=models.CharField(blank=True, max_length=7, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='business_line',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='business_line',
            name='slug',
            field=models.SlugField(db_index=False, max_length=80),
        ),
        migrations.AlterField(
            model_name='business_line',
            name='uniquefield',
            field=models.CharField(blank=True, max_length=8, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='business_signup',
            name='name',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='business_signup',
            name='slug',
            field=models.SlugField(blank=True, db_index=False),
        ),
        migrations.AlterField(
            model_name='user_signup',
            name='first_name',
            field=models.CharField(blank=True, default='Lanre', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user_signup',
            name='last_name',
            field=models.CharField(blank=True, default='ojetokun', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user_signup',
            name='ticket',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddIndex(
            model_name='business_signup',
            index=models.Index(fields=['name', 'address', 'state'], name='account_bus_name_fcb6bc_idx'),
        ),
        migrations.AddField(
            model_name='special_line',
            name='admin_user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_special_line', to='account.user_signup'),
        ),
        migrations.AddField(
            model_name='orders',
            name='business',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='not_important', to='account.business_signup'),
        ),
        migrations.AddField(
            model_name='orders',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_orders', to='account.user_signup'),
        ),
        migrations.AddField(
            model_name='items',
            name='business',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_items', to='account.business_signup'),
        ),
        migrations.AddField(
            model_name='user_signup',
            name='special_line',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='all_present', to='account.special_line'),
        ),
    ]
