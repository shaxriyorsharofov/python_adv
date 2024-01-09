from django.urls import path
from .views import get_name

urlpatterns = [
    path('name/', get_name)
]