from django.conf.urls import url
from django.contrib.admindocs import views
from main import views

urlpatterns=[
    url('main/',views.main,name='main')
]