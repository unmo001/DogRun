from django.urls import path

from . import views

app_name = 'Owner'

urlpatterns = [
    path('home/', views.HomeView,name='HomeView'),
    path('', views.index, name='index'),
]
