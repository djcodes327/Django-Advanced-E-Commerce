# Generated by Django 3.1.3 on 2020-12-01 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0008_orders'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orders',
            options={'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterModelTable(
            name='orders',
            table='orders',
        ),
    ]
