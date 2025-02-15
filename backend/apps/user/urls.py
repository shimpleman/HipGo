# backend/apps/user/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # 定义用户应用的路由
    path('list/', views.UserListView.as_view(), name='user-list'),
    # 添加更多路由...
]