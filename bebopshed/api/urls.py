from django.urls import path
from .views import main, generate_line

urlpatterns = [
    path('', main),
    path('api/generate', generate_line)
]