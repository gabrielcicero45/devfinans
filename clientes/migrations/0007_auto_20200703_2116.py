# Generated by Django 3.0.8 on 2020-07-04 00:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_cliente_senha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='cidade',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='endereco',
        ),
    ]