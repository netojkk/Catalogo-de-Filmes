from django.shortcuts import render
from django.http import  JsonResponse, HttpResponse
from django.conf import settings


# Create your views here.
def home(request):
    return render(request, "index.html")

def buscar_filmes(request):
    
    busca_titulo = request.GET.get('title')
    
    if not busca_titulo:
        return JsonResponse({"error": "Forneça um termo de busca."}, status = 400)
    
    url = f'http://www.omdbapi.com/?apikey={settings.MY_API_KEY}&'
    
    response = request.get(url)
    
    if response.status.code == 200:
        data = response.json()
        return JsonResponse(data)
    else:
        return JsonResponse({"error": "Não foi possivel encontrar o filme!"}, status=500)
    
def testar_api(request):
    # URL da API
    url = f"http://www.omdbapi.com/?apikey={settings.MY_API_KEY}&s=Inception"
    
    # Faz a requisição para a API
    response = request.get(url)
    
    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        data = response.json()  # Converte a resposta para JSON
        return JsonResponse(data)  # Retorna os dados da API
    else:
        return JsonResponse({"error": "Não foi possível conectar à API."}, status=response.status_code)