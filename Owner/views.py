from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def index(request):
    return render(request, 'registration/index.html')


class HomeView(TemplateView):
    template_name = 'home.html'
