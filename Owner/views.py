from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Owner


# Create your views here.
def index(request):
    return render(request, 'registration/index.html')









