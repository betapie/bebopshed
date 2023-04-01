from django.urls import path
from .views import main, generate_line, generate_chops_build

urlpatterns = [
    path("", main),
    path("generate", generate_line),
    path("chops_builder", generate_chops_build)
]
