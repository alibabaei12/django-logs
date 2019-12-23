from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('log_files', views.log_files, name="logs"),
    path('cd_folder', views.cd_folder, name="cd_folder"),
    path('file_view', views.file_view, name="file_view"),
    path('connect_page', views.connect_page, name = "connect")
]
