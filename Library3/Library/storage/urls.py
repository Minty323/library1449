from django.urls import path
from . import views
urlpatterns = [
    path('', views.storage_home, name='storage_home'),
    path('create', views.create, name='create'),


]