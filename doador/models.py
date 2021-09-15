from django.db import models

class Entidade (models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.CharField('Email', max_length=150)

    def __str__(self):
        return self.nome

class Especie (models.Model):
    nome  = models.CharField('Nome', max_length=100)
    descricao = models.CharField('Descrição', max_length=150)

    def __str__(self):
        return self.nome

class Raca (models.Model):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.CharField('Descrição', default="", max_length=150)
    especie = models.ForeignKey(Especie, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nome

class Animal (models.Model):
    nome = models.CharField('Nome', max_length=50)
    idade = models.IntegerField('Idade')
    raca = models.ForeignKey(Raca, on_delete=models.RESTRICT)
    entidade = models.ForeignKey(Entidade, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nome
