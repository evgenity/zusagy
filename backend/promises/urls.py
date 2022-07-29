from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('how', views.how, name='how'),
    path('create', views.create, name='create'),
    path('final', views.final, name='final'),
    path('report', views.report, name='report'),
]