from django.urls import path

from . import views

urlpatterns = [
    #ruta, vista, nombre interno
    path('',views.index, name='index'),
    path('clases/',views.clases, name='clases')
]