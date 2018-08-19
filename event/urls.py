from django.urls import path

from . import views

app_name = 'event'
urlpatterns = [
    # ex: /event/
    path('', views.index, name='index'),
    # ex: /event/5/
    path('<int:event_id>/', views.detail, name='detail'),
    path('add/', views.add, name='add'),
]
