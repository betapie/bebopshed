from django.urls import path
from .views import index

urlpatterns = [
    path("", index),
    path("about", index),
    path("contribute", index),
    path("legal_notice", index)
]
