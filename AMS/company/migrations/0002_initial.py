# Generated by Django 5.1.1 on 2024-09-24 05:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='added_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.companyusers'),
        ),
        migrations.AddField(
            model_name='expense',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='company.company'),
        ),
        migrations.AddField(
            model_name='income',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incomes', to='company.company'),
        ),
    ]
