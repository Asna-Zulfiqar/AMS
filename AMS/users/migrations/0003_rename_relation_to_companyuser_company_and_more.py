# Generated by Django 5.1.1 on 2024-09-24 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0002_rename_companyusers_companyuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companyuser',
            old_name='relation_to',
            new_name='company',
        ),
        migrations.AddField(
            model_name='companyuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='companyuser_set', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='companyuser',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='companyuser',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='companyuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='companyuser_set', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='companyuser',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='companyuser',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='companyuser',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='companyuser',
            name='username',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
