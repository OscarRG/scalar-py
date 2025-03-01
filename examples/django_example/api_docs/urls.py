from django.urls import path
from .views import api_docs

urlpatterns = [
    path('pet/', api_docs, name='api_docs'),
]
