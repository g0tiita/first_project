#definir rutas de la App "blogs"
from django.urls import path   
from . import views

urlpatterns = [
    #path('', views.index),	   
    #path('adios', views.adios),	 
    path('blogs', views.root),
    path('blogs/new', views.new),	 
    path('blogs/create', views.create),	
    path('blogs/<number>', views.show),	
    path('blogs/<number>/edit', views.edit),	
    path('blogs/<number>/delete', views.destroy),
    #al poner el blogs/json me redirije a las anteriores
    path('', views.profile),

]
