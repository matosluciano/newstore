# Generated by Django 5.0.6 on 2024-05-22 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=60),
        ),
    ]