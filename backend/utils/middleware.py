# backend/utils/middleware.py
from django.utils.deprecation import MiddlewareMixin

class CustomMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # 可以在这里添加处理请求的逻辑
        pass

    def process_response(self, request, response):
        # 可以在这里添加处理响应的逻辑
        return response