from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<game_name>[\w]+)/$', views.game, name='game')
]
