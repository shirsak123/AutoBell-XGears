# Generated by Django 3.1.13 on 2021-08-18 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20210313_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('In Progress', 'In Progress'), ('Delivered', 'Delivered'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Pending', max_length=15),
        ),
    ]