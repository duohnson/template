from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),

]

'''

NoReverseMatch - si sale este error, revise name en urls 
que coincida con views.

'''