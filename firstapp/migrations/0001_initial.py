# Generated by Django 2.0.6 on 2019-09-24 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('UserFullName', models.CharField(default='', max_length=200)),
                ('UserEmail', models.CharField(default='', max_length=200, primary_key=True, serialize=False)),
                ('UserPassword', models.CharField(default='', max_length=200)),
                ('UserMobile', models.BigIntegerField()),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('roleId', models.AutoField(primary_key=True, serialize=False)),
                ('roleName', models.CharField(default='', max_length=200)),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='siteuser',
            name='roleId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.UserRole'),
        ),
    ]
