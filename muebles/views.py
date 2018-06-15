# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from muebles.models import Mueble, Categoria, Imagen
from django.shortcuts import render, get_object_or_404,render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.forms import modelform_factory
from django.contrib import messages
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.decorators import login_required

def vermuebles(request):
    muebles = Mueble.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'muebles/allmuebles.html', {'muebles': muebles,'categorias':categorias})

def vermueble(request, mueble_id):
    mueble = get_object_or_404(Mueble, pk=mueble_id)
    return render(request, 'muebles/mueble.html', {'mueble':mueble})

#@login_required
def intro_edit_mueble(request, mueble_id=None):
    es_modificacio =(mueble_id!=None)
    muebleForm =modelform_factory(Mueble,exclude=('id','usuario',))
    if es_modificacio:
        mueble = get_object_or_404(Mueble, id=mueble_id)
    else:
        mueble =Mueble()
    if request.method == 'POST':
        form = muebleForm(request.POST,request.FILES,instance=mueble)
        if form.is_valid():
            form.instance.usuario = request.user
            mueble = form.save()
            if(es_modificacio):
                messages.add_message(request, messages.SUCCESS, 'Modificado correctamente')
            else:
                messages.add_message(request, messages.SUCCESS, 'Creado correctamente ')
            return HttpResponseRedirect(reverse('muebles:ver_muebles'))
        else:
            if(es_modificacio):
                messages.add_message(request, messages.ERROR, 'Error en la modificacion del mueble')
            else:
                messages.add_message(request, messages.ERROR, 'Error en crear el mueble')
    else:
        form = muebleForm(instance=mueble)

    form.helper = FormHelper()
    form.helper.form_class = 'form-horizontal col-md-8 col-md-offset-2'
    form.helper.label_class = 'col-lg-3'
    form.helper.field_class = 'col-lg-8 col-md-8'
    form.helper.add_input(Submit('submit', 'Enviar'))
    return render(request, 'formulario.html', {'form': form, 'mueble':mueble})

#@login_required
def eliminarmueble(request, mueble_id):
    mueble = get_object_or_404(Mueble, pk=mueble_id)
    messages.add_message(request, messages.SUCCESS,'El mueble he sido borrado correctamente')
    mueble.delete()
    return HttpResponseRedirect(reverse('muebles:ver_muebles') )



#categorias

def vercategorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'muebles/categorias.html', {'categorias': categorias})

#@login_required
def intro_edit_categoria(request, categoria_id=None):
    es_modificacio =(categoria_id!=None)
    categoriaForm =modelform_factory(Categoria,exclude=('id','usuario',))
    if es_modificacio:
            categoria = get_object_or_404(Categoria, id=categoria_id)
    else:
        categoria =Categoria()
    if request.method == 'POST':
        form = categoriaForm(request.POST,request.FILES,instance=categoria)
        if form.is_valid():
            form.instance.usuario = request.user
            categoria = form.save()
            if(es_modificacio):
                messages.add_message(request, messages.SUCCESS, 'Modificado correctamente')
            else:
                messages.add_message(request, messages.SUCCESS, 'Creado correctamente ')
            return HttpResponseRedirect(reverse('muebles:ver_categorias'))
        else:
            if(es_modificacio):
                messages.add_message(request, messages.ERROR, 'Error en la modificacion de la categoria')
            else:
                messages.add_message(request, messages.ERROR, 'Error en crear la categoria')
    else:
        form = categoriaForm(instance=categoria)

    form.helper = FormHelper()
    form.helper.form_class = 'form-horizontal col-md-8 col-md-offset-2'
    form.helper.label_class = 'col-lg-3'
    form.helper.field_class = 'col-lg-8 col-md-8'
    form.helper.add_input(Submit('submit', 'Enviar'))
    return render(request, 'formulario.html', {'form': form, 'categoria':categoria})

#@login_required
def eliminarcategoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    messages.add_message(request, messages.SUCCESS,'El mueble he sido borrado correctamente')
    categoria.delete()
    return HttpResponseRedirect(reverse('muebles:ver_categorias') )


#imagenes
#@login_required
def verimagenes(request):
    imagenes = Imagen.objects.all()
    return render(request, 'muebles/imagen.html', {'imagenes': imagenes})

#@login_required
def intro_edit_imagen(request, imagen_id=None):
    es_modificacio =(imagen_id!=None)
    imagenForm =modelform_factory(Imagen,exclude=('id',))
    if es_modificacio:
        imagen = get_object_or_404(Imagen, id=imagen_id)
    else:
        imagen=Imagen()
    if request.method == 'POST':
        form = imagenForm(request.POST,request.FILES,instance=imagen)
        if form.is_valid():
            imagen = form.save()
            if(es_modificacio):
                messages.add_message(request, messages.SUCCESS, 'Modificado correctamente')
            else:
                messages.add_message(request, messages.SUCCESS, 'Creado correctamente ')
            return HttpResponseRedirect(reverse('muebles:ver_imagenes'))
        else:
            if(es_modificacio):
                messages.add_message(request, messages.ERROR, 'Error en la modificacion de la imagen')
            else:
                messages.add_message(request, messages.ERROR, 'Error en crear la imagen')
    else:
        form = imagenForm(instance=imagen)

    form.helper = FormHelper()
    form.helper.form_class = 'form-horizontal col-md-6 col-md-offset-3'
    form.helper.label_class = 'col-lg-3'
    form.helper.field_class = 'col-lg-8 col-md-8'
    form.helper.add_input(Submit('submit', 'Enviar'))
    return render(request, 'formulario.html', {'form': form, 'imagen':imagen})

#@login_required
def eliminarimagen(request, imagen_id):
    imagen = get_object_or_404(Imagen, pk=imagen_id)
    messages.add_message(request, messages.SUCCESS,'La Imagen he sido borrado correctamente')
    imagen.delete()
    return HttpResponseRedirect(reverse('muebles:ver_imagenes') )




def index(request):
    return render_to_response('muebles/home.html')

def contacte(request):
    return render_to_response('muebles/contacte.html')

def oferta(request):
    return render_to_response('muebles/oferta.html')
