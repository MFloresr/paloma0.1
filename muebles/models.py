# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Categoria (models.Model):
    id = models.AutoField(primary_key = True, unique = True)
    nombre_categoria = models.CharField(max_length=(100),help_text="Nombre de la categoria")
    def __str__(self):
        return '%s' % (self.nombre_categoria)

class Mueble (models.Model):
    id = models.AutoField(primary_key = True, unique = True)
    Marca = models.CharField(max_length=100,help_text="Marca del Mueble")
    nombre_mueble = models.CharField(max_length=100,help_text="El nombre del mueble")
    precio = models.DecimalField(decimal_places=2,max_digits=5,help_text="precio del mueble")
    imagen = models.ImageField(upload_to='imagenes')
    categoria = models.ForeignKey(Categoria)
    def __str__(self):
        return '%s' % (self.nombre_mueble)

class Imagen (models.Model):
    id = models.AutoField(primary_key = True, unique = True)
    titulo = models.CharField(max_length=100,help_text="El titulo de la imagen")
    imagen = models.ImageField(upload_to='imagenes')
    def __str__(self):
        return '%s' % (self.titulo)