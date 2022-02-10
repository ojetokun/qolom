# Generated by Django 3.1 on 2020-09-15 21:57

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
            name='Business_line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=250)),
                ('uniquefield', models.CharField(blank=True, max_length=80, null=True)),
                ('slug', models.SlugField(max_length=200)),
                ('opentime', models.DateTimeField(blank=True, null=True)),
                ('closetime', models.DateTimeField(blank=True, null=True)),
                ('openday', models.CharField(blank=True, max_length=200, null=True)),
                ('closeday', models.CharField(blank=True, max_length=200, null=True)),
                ('offset', models.CharField(blank=True, max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=80, null=True)),
                ('password', models.CharField(max_length=80, null=True)),
                ('email', models.CharField(max_length=250, null=True)),
                ('first_name', models.CharField(max_length=250, null=True)),
                ('last_name', models.CharField(max_length=250, null=True)),
                ('ticket', models.CharField(blank=True, max_length=30)),
                ('time', models.DateTimeField(blank=True, null=True)),
                ('country', models.CharField(max_length=300, null=True)),
                ('iso_code', models.CharField(max_length=2, null=True)),
                ('present_line', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='people_present', to='account.business_line')),
                ('user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_signup', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Business_signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=80, null=True)),
                ('password', models.CharField(max_length=80, null=True)),
                ('email', models.CharField(max_length=250, null=True)),
                ('name', models.CharField(max_length=80)),
                ('slug', models.SlugField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('address', models.CharField(max_length=300, null=True)),
                ('state', models.CharField(max_length=300, null=True)),
                ('country', models.CharField(max_length=300, null=True)),
                ('iso_code', models.CharField(max_length=2, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='business_signup', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='business_line',
            name='business',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business_line', to='account.business_signup'),
        ),
    ]
