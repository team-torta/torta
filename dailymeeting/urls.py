from django.urls import path

from . import views

app_name = 'dailymeeting'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.DayCreateView.as_view()),
]
