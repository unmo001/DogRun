from django.urls import path

from . import views

app_name = 'Owner'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.HomeView.as_view(), name='HomeView'),
]
