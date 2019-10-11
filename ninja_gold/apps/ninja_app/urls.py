from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_money/(?P<name>\w+)$', views.process),
    url(r'^winning_conditions$', views.winning_conditions),
    url(r'^reset$', views.reset),
]