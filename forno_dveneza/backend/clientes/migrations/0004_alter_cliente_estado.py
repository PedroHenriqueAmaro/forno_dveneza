# Generated by Django 4.1.7 on 2023-05-09 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_cliente_complemento_cliente_data_cadastro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='estado',
            field=models.CharField(choices=[('SP', 'São Paulo'), ('NI', 'Não informado')], max_length=2),
        ),
    ]