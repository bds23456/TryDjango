from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('button', views.but, name='button')

]
