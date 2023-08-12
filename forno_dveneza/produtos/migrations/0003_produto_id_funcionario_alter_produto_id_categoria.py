# Generated by Django 4.1.7 on 2023-05-06 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0002_cargo_funcionario_data_cadastro_funcionario_estado_and_more'),
        ('produtos', '0002_alter_produto_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='id_funcionario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='funcionarios.funcionario'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='id_categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='produtos.categoria'),
        ),
    ]