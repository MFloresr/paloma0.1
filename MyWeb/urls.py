# encoding: utf-8
from __future__ import unicode_literals

from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView
import muebles

urlpatterns = ([
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='muebles/home.html'), name='index'),
    url(r'^muebles/', include('muebles.urls', namespace='muebles')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--
    url(r'^contacte/$', TemplateView.as_view(template_name='muebles/contacte.html'), name='contacte'),
    url(r'^oferta-del-mes/$', TemplateView.as_view(template_name='muebles/oferta.html'), name='oferta'),
])