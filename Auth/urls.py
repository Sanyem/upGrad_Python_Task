from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.auth.views import logout

app_name = 'Auth'

urlpatterns = [
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^$', views.login, name="login"),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
]