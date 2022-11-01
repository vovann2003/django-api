from django.urls import path
from .views import FileAPIView, FileInfoAPI, FileInfoCsv


urlpatterns = [
    path('api/', FileAPIView.as_view(), name='file-api'),
    path('api/file-info/', FileInfoAPI.as_view(), name='file_info-api'),
    path('api/file-info/csv', FileInfoCsv.as_view(), name='file_info-csv'),
]
