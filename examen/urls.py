from django.urls import path
from . import views

app_name = 'examen'

urlpatterns = [
    path('',views.Index, name='pregunta'),
    path('resultado',views.Resultado, name='result'),
    path('lista/', views.Alumnos, name='list')
]