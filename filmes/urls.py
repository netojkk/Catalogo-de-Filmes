from django.urls import path
from .views import home, testar_api

urlpatterns = [
    path('', home),
    path('testar-api/', testar_api, name='testar-api')
]
