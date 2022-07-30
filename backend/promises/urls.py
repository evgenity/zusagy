from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('how', views.how, name='how'),
    path('create', views.create, name='create'),
    path('final/<str:short_link>', views.final, name='final'),
    path('r/<str:short_link>', views.report, name='report'),
    path('u/<str:short_link>', views.report_upload, name='report_upload')
]