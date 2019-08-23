from django.db import models

# Create your models here.
class Estabelecimento(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200, null=False)
    endereco = models.CharField(max_length=200, null=False)
    complemento = models.CharField(max_length=100, null=True)
    cnpj = models.CharField(max_length=20, null=False)
    telefone = models.CharField(max_length=20, null=True)
    
