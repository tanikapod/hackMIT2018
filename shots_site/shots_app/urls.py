from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('create/', views.create, name = 'create'),
    path('<int:game_id>/', views.game_detail, name = 'game'),
    path('play/', views.play, name = 'play')
]
