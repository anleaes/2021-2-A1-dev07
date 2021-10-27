from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.login, name='login'),
    path('login', views.login, name='login'),
    path('home', views.home, name='home'),
    path('filmes', views.filmes, name='filmes'),
    path('series', views.series, name='series'),
    path('documentarios', views.documentarios, name='documentarios'),
    path('planos', views.planos, name='planos'),
]