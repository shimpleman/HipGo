# backend/apps/about/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # 定义用户应用的路由
    path('list/', views.AboutListView.as_view(), name='about-list'),
    # 添加更多路由...
]