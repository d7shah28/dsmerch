# Generated by Django 3.2 on 2022-07-05 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='tax_percent',
            field=models.DecimalField(blank=True, decimal_places=2, default=18.0, max_digits=10, null=True, verbose_name='Tax Percent'),
        ),
        migrations.AlterField(
            model_name='order',
            name='tax_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, verbose_name='Tax Price'),
        ),
    ]
