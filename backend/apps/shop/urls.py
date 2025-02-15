# backend/apps/shop/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # 定义用户应用的路由
    path('list/', views.ShopListView.as_view(), name='shop-list'),
    # 添加更多路由...
]