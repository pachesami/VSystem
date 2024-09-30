# VSystem/urls.py
from django.contrib import admin
from django.urls import path, include
from curso.views import get_curso  # Asegúrate de que esta función exista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cursos/<int:curso_id>/', get_curso, name='get_curso'),
]
