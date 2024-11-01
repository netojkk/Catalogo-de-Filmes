from django.shortcuts import render
from django.http import  JsonResponse, HttpResponse
from django.conf import settings


# Create your views here.
def home(request):
    return render(request, "index.html")

def buscar_filmes(request):
    url = 'http://www.omdbapi.com/?apikey={settings.API_KEY}&'