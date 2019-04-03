from django.conf.urls import url, include
from django.contrib import admin

from . import views

app_name = 'schedule'

urlpatterns = [
    url(r'^$', views.dashboard, name="dashboard"),
    url(r'^add-schedule/$', views.addSchedule, name="add-schedule"),
    url(r'^update-schedule/(?P<id>[0-9])/$', views.updateSchedule, name="update-schedule"),
    url(r'^delete-schedule/(?P<id>[0-9])/$', views.deleteSchedule, name="delete-schedule"),
    url(r'^mark/(?P<id>[0-9])/(?P<val>[0-9])$', views.mark, name="mark"),
]
