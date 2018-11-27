from django.shortcuts import render

# Create your views here.
# import de Vistas Basadas en clases para CRUDS Basicos
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Import de Formularios
from apps.modelos.forms import *
# Import de Modelos
from apps.modelos.models import *

class EscuelaIndex(TemplateView):
    template_name = "index.html"