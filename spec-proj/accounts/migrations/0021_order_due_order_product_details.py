# Generated by Django 4.0.3 on 2022-07-24 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='due',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='product_details',
            field=models.CharField(blank=True, default='None:', max_length=200, null=True),
        ),
    ]
