# backend/apps/admin/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # 定义用户应用的路由
    path('list/', views.AdminListView.as_view(), name='admin-list'),
    # 添加更多路由...
]