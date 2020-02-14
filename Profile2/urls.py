from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
# from rest_framework import routers, serilizers, viewsets
from Profile2 import views

urlpatterns = [
    re_path(r'profile_lista/$', views.Profile2List.as_view()),
    re_path(r'estado_lista/$', views.EstadoList.as_view()),
    re_path(r'ciudad_lista/$', views.CiudadList.as_view()),
    re_path(r'genero_lista/$', views.GeneroList.as_view()),
    re_path(r'ocupacion_lista/$', views.OcupacionList.as_view()),
    re_path(r'estadocivil_lista/$', views.EstadoCivilList.as_view()),
]