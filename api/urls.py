from django.urls import path
from .views import FileView, FileDownload, GEOPointView

urlpatterns = [
    path('point/', GEOPointView.as_view()),
    path('pointload/', FileDownload.as_view()),
    path('upload/', FileView.as_view(), name='file_upload')
]
