# backend/apps/blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # 定义用户应用的路由
    path('list/', views.BlogListView.as_view(), name='blog-list'),
    # 添加更多路由...
]