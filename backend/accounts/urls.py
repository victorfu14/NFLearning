from django.urls import use;

from . import views;

urlpatters = {
        url(r'^signup/', views.SignUp.as_view(), name ='signup'),
