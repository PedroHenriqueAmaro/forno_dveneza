from typing import List

from django.db import models

from clientes.models import Cliente
from produtos.models import Produto


# Create your models here.

class Carrinho(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    itens = models.ManyToManyField('ItemCarrinho', null=True, blank=True)

    def __str__(self):
        return f'{self.cliente} {self.itens}'


class ItemCarrinho(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def __str__(self):
        return f'{self.produto} {self.quantidade}'
