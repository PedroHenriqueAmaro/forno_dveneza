# Generated by Django 4.1.7 on 2023-03-26 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='foto',
            field=models.CharField(choices=[('/static/base/img/coca.png', 'Refrigerante'), ('/static/base/img/pizza.png', 'Pizza')], max_length=40),
        ),
    ]
