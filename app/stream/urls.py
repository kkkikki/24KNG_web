from django.urls import path
from . import views

urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('video/<int:video_id>/', views.video_player, name='video_player'),
]
