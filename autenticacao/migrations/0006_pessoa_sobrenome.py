# Generated by Django 4.1.5 on 2023-01-24 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0005_pedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='sobrenome',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
