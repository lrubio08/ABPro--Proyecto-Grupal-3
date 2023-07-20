from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='mensaje'),
    path('clientes/', views.clientes, name='clientes' )
    
]
