from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('how', views.how, name='how'),
    path('methods', views.methods, name='methods'),
    path('profits', views.profits, name='profits'),
    path('create', views.create, name='create'),
    path('new', views.new, name='new'),
    path('advices', views.advices, name='advices'),
    path('final/<str:short_link>', views.final, name='final'),
    path('r/<str:short_link>', views.report, name='report'),
    path('u/<str:short_link>', views.report_upload, name='report_upload')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)