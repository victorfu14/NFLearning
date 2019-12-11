from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^$', views.view_home, name='home'),
    url(r'^feedback/', views.feedback, name='feedback'),
    url(r'^current_games/', views.current_games, name='current_games')
]
