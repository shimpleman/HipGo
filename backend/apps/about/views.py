# backend/apps/about/views.py
from rest_framework.views import APIView
from rest_framework.response import Response

class AboutListView(APIView):
    def get(self, request):
        # 获取用户列表的逻辑
        return Response({"message": "About list"})