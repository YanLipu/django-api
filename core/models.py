from django.db import models

# Create your models here.
class Grupo(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    status = models.BooleanField()
    data_criacao = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    nome_completo = models.CharField(max_length=50)
    data_nascimento = models.CharField(max_length=50)
    sexo = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    logradouro = models.CharField(max_length=50)
    status = models.BooleanField()
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.nome_completo
    
