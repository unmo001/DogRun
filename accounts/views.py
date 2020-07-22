from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView as AuthLoginView
from django.contrib.auth.models import User
from django.views.generic import CreateView
from .forms import UserCreateForm


# Create your views here.
class LoginView(AuthLoginView):
    template_name = 'registration/login.html'


login = LoginView.as_view()


class CreateAccounts(CreateView):
    def post(self, request, *args, **kwargs):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        return render(request, 'registration/create.html', {'form': form, })

    def get(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        return render(request, 'registration/create.html', {'form': form, })


CreateAccounts = CreateAccounts.as_view()
