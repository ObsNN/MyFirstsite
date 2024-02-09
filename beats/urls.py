from django.urls import path
from . import views

urlpatterns = [
    path('', views.music, name='music'),
    path('post/<int:pk>/', views.post_detail, name='post_detail')
]