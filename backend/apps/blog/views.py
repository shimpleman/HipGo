# backend/apps/blog/views.py
from rest_framework.views import APIView
from rest_framework.response import Response

class BlogListView(APIView):
    def get(self, request):
        # 获取用户列表的逻辑
        return Response({"message": "Blog list"})