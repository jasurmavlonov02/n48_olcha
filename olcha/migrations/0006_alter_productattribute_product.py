# Generated by Django 5.1.1 on 2024-09-26 12:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olcha', '0005_attributekey_key_name_attributevalue_value_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productattribute',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attributes', to='olcha.product'),
        ),
    ]
