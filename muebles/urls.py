from django.conf.urls import url
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    #pagina principal
    url(r'^$', views.index, name='index'),

    #muebles
    url(r'^(?P<mueble_id>[0-9]+)/$', views.vermueble, name='ver_mueble'),
    url(r'^nuevomueble/$', views.intro_edit_mueble, name='nuevo_mueble'),
    url(r'^editarmueble/(?P<mueble_id>[0-9]+)/$', views.intro_edit_mueble, name='editar_mueble'),
    url(r'^eliminarmueble/(?P<mueble_id>[0-9]+)/$', views.eliminarmueble, name='eliminar_mueble'),

    #categoria
    url(r'^categorias/$', views.vercategorias, name='ver_categorias'),
    url(r'^introduircategorias/$', views.intro_edit_categoria, name='nueva_categoria'),
    url(r'^editarcategoria/(?P<categoria_id>[0-9]+)/$', views.intro_edit_categoria, name='editar_categoria'),
    url(r'^eliminarcategoria/(?P<categoria_id>[0-9]+)/$', views.eliminarcategoria, name='eliminar_categoria'),




]

