from django.urls import path

from .views import index, simple_api_view

urlpatterns = [
    path('', index, name='index'),
    path('api/phrases/', simple_api_view, name='phrases'),
]