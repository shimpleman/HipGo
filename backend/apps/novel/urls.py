# backend/apps/novel/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # 定义用户应用的路由
    path('list/', views.NovelListView.as_view(), name='novel-list'),
    # 添加更多路由...
]