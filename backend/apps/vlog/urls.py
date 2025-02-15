# backend/apps/vlog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # 定义用户应用的路由
    path('list/', views.VlogListView.as_view(), name='vlog-list'),
    # 添加更多路由...
]