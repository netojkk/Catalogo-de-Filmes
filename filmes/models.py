from django.db import models
from django.http import JsonResponse

# Create your models here.
class Filmes(models.Model):
    title = models.CharField(max_length=200)
    ano = models.CharField(max_length=4)
    image = models.URLField(max_length=300, blank=True, null=True)
    
    def __str__(self):
        return self.title
    # def get(self, request):
    #     movies = [
    #         {
    #             "title": "Procurando Nemo", 
    #             "image": "https://via.placeholder.com/150",
    #             "year":"2010"
    #         },
    #         {
    #             "title": "Anjos da Noite",
    #             "image": "https://via.placeholder.com/150",
    #             "year":"2012"
    #         },
    #         {
    #             "title": "Lorax",
    #             "image": "https://via.placeholder.com/150",
    #             "year":"2007"
    #         },
    #         {
    #             "title": "Barbie",
    #             "image": "https://via.placeholder.com/150",
    #             "year":"2010"
    #         },
    #     ]
    #     return JsonResponse(movies, safe=False)