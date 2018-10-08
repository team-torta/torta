from django.urls import path

from . import views

app_name = 'jma'
urlpatterns = [
    path('', views.index, name='index'),
    path('feedList', views.feedList, name='feedList'),
    path('analysis', views.analysis, name='analysis'),
    path('aci_data.json', views.aci_data, name='aci_data'),
    path('eq_data.json', views.eq_data, name='eq_data'),
]
