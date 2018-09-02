from django.urls import path

from . import views

app_name = 'dailymeeting'
urlpatterns = [
    path('', views.index, name='index'),
    path('grouping', views.grouping, name='grouping'),
    path('get_group/<int:mode>', views.get_group, name='get_group'),
    path('create', views.DayCreateView.as_view()),
]
