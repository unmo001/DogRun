from django.urls import path

from . import views
from accounts.views import CreateAccounts

app_name = 'Owner'

urlpatterns = [
    path('home/', CreateAccounts, name='CreateAccounts'),
    path('', views.index, name='index')
]
