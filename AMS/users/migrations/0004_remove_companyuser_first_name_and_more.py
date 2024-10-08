# Generated by Django 5.1.1 on 2024-09-25 06:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_relation_to_companyuser_company_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyuser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='companyuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='companyuser',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='companyuser',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='companyuser',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='companyuser',
            name='password',
        ),
        migrations.RemoveField(
            model_name='companyuser',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='companyuser',
            name='username',
        ),
        migrations.AddField(
            model_name='companyuser',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
