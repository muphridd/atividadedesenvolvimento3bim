from django.contrib import admin
from django.urls import path, include
from livros.views import pagina_inicial

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pagina_inicial, name='pagina_inicial'),  
    path('autores/', include('livros.urls')),  
]
