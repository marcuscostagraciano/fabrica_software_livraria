# Generated by Django 5.0.3 on 2024-03-23 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livraria', '0004_itenscompra'),
    ]

    operations = [
        migrations.AddField(
            model_name='itenscompra',
            name='preco_item',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
