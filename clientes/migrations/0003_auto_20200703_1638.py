# Generated by Django 3.0.8 on 2020-07-03 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20200703_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='senha',
            field=models.CharField(default='0000000', max_length=8),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Email',
        ),
    ]
