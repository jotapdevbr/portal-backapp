from django.db import models

class Link(models.Model):
    nome = models.CharField(max_length=255)
    url = models.URLField()
    departamento = models.CharField(max_length=255, choices=[
        ('TI', 'TI'),
        ('RH', 'RH'),
        ('SSO', 'SS0'),
        ('FISCAL', 'FISCAL'),
        ('LOGISTICA', 'LOGISTICA'),
        ('GERAL', 'GERAL'),
        ('OUTROS', 'OUTROS'),

    ])
    descricao = models.TextField(blank=True)

class Programa(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)
    link_download = models.URLField(blank=True)
    arquivo = models.FileField(upload_to='programas/', blank=True)
    departamento = models.CharField(max_length=255, choices=[
        ('LOGISTICA', 'LOGISTICA'),
        ('GERAL', 'GERAL'),
        ('TI', 'TI'),
        ('RH', 'RH'),
        ('SSO', 'SSo'),
        ('FISCAL', 'FISCAL'),
        ('OUTROS', 'OUTROS'),
    ])
    icone = models.ImageField(upload_to='icones/', blank=True) 

class Manual(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)
    link_download = models.URLField(blank=True)
    arquivo = models.FileField(upload_to='manuais/', blank=True)
    departamento = models.CharField(max_length=255, choices=[
        ('GERAL', 'GERAL'),
        ('TI', 'TI'),
        ('RH', 'RH'),
        ('SSO', 'SS0'),
        ('FISCAL', 'FISCAL'),
        ('LOGISTICA', 'LOGISTICA'),
        ('OUTROS', 'OUTROS'),
    ])
    icone = models.ImageField(upload_to='icones/', blank=True)