from django.db import models

class Entidade (models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.CharField('Email', max_length=150)
