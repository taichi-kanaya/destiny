from django.conf.urls import url

from . import views

app_name = 'top'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^telling$', views.telling, name='telling'),
]