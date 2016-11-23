from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.HomePage, name='HomePage'),
    url(r'^upload/$', views.upload, name='upload'),
]