from django.conf.urls import url
from . import views

app_name='kolej'

urlpatterns=[
    url(r'^$' ,views.index, name='index'),
    url(r'^faculty', views.prof,name='faculty'),
    url(r'^Gallery', views.prof,name='professor')
]