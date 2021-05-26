from django.urls import path
from . import views

urlpatterns = [
    path('', views.post, name='post'),
    path('<slug:slug>/', views.detail_post, name='detail_post'),
]
