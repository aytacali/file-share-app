from django.urls import path
from . import views

app_name = "file"

urlpatterns = [
    path('', views.home_view, name = 'home'),
    path('upload/', views.upload_file, name='upload_file'),
    path('file/<int:id>/', views.file_detail_view, name="file_detail"),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
]