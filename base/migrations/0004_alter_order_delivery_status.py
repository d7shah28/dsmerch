# Generated by Django 3.2 on 2022-06-26 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20220607_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_status',
            field=models.CharField(blank=True, choices=[('NOT_DISPATCHED', 'Not Dispatched'), ('DISPATCHED', 'Dispatched'), ('OTW', 'On The Way'), ('DELIVERED', 'Delivered')], default=None, max_length=30, verbose_name='Payment method'),
        ),
    ]