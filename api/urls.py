from django.urls import path
from .views import *

urlpatterns=[
    path('point/',GEOPointView.as_view()),
]