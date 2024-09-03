# Generated by Django 5.1 on 2024-09-02 01:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounting', '0001_initial'),
        ('frontdesk', '0001_initial'),
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bills',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='frontdesk.customer'),
        ),
        migrations.AddField(
            model_name='employeesalary',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.empoyee'),
        ),
        migrations.AddField(
            model_name='payment',
            name='bill',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounting.bills'),
        ),
    ]
