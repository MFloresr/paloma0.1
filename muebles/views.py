# -*- coding: utf-8 -*-
from muebles.models import Mueble, Categoria
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
    return render(request, 'muebles/allmuebles.html', {'muebles': muebles})

def vermueble(request, mueble_id):
    mueble = get_object_or_404(Mueble, pk=mueble_id)
    return render(request, 'muebles/mueble.html', {'noticia':mueble})

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
            return HttpResponseRedirect(reverse('noticias:ver_noticias'))
        else:
            if(es_modificacio):
                messages.add_message(request, messages.ERROR, 'Error en la modificacion de la noticia')
            else:
                messages.add_message(request, messages.ERROR, 'Error en crear la noticia')
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
    return HttpResponseRedirect(reverse('noticias:ver_noticias') )



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
                messages.add_message(request, messages.ERROR, 'Error en la modificacion de la noticia')
            else:
                messages.add_message(request, messages.ERROR, 'Error en crear la noticia')
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




def index(request):
    return render_to_response('muebles/home.html')

def contacte(request):
    return render_to_response('muebles/contacte.html')

def oferta(request):
    return render_to_response('muebles/oferta.html')
