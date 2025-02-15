# backend/utils/response.py
from rest_framework.response import Response

def success_response(data=None, message="Request successful"):
    return Response({"message": message, "data": data}, status=200)

def error_response(data=None, message="Request failed", status=400):
    return Response({"message": message, "data": data}, status=status)