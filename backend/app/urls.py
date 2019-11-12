from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^$', views.view_home, name='home'),
    url(r'^feedback/', views.feedback, name='feedback')
]
