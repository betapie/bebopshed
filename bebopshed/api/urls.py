from django.urls import path
from .views import main, generate_line

urlpatterns = [
    path('', main),
    path('generate', generate_line)
]