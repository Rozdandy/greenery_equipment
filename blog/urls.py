from django.urls import path
from . import views

urlpatterns = [
    path('', views.post, name='post'),
    path('blog_add/', views.blog_add, name='blog_add'),
    path('<slug:slug>/', views.detail_post, name='detail_post'),
    path('category/<slug:slug>/', views.category, name='category'),
    path('edit_blog/<slug:slug>/', views.edit_blog, name='edit_blog'),
    path('delete_blog/<slug:slug>/', views.delete_blog, name='delete_blog'),
]
