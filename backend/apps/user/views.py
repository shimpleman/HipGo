# backend/apps/user/views.py
from rest_framework.views import APIView
from rest_framework.response import Response

class UserListView(APIView):
    def get(self, request):
        # 获取用户列表的逻辑
        return Response({"message": "User list"})