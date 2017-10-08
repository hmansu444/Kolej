from django.conf.urls import url
from . import views

app_name='kolej'

urlpatterns=[
    url(r'^$' ,views.index, name='index'),
<<<<<<< HEAD
    url(r'^faculty', views.prof,name='faculty')
=======
    url(r'^/Gallery', views.prof,name='professor')
>>>>>>> 44c49a90d819538a7d4c468551e52bb04c6735bc
]