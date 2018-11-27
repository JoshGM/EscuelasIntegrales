from django.urls import path
# Import de vistas del sitio
from .views import EscuelaIndex
# Import de vistas para Iniciar Sesion y cerrar sesion
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Pagina principal del sitio
    path('', EscuelaIndex.as_view(), name='index'),
    # URLS para iniciar sesion y finalizar sesion
    path('login/', LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]