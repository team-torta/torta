from django.urls import path

from . import views

app_name = 'jma'
urlpatterns = [
    path('', views.index, name='index'),
]
