from django.urls import path

from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('createaccounts/', views.CreateAccounts, name='CreateAccount')
]
