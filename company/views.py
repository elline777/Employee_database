"""Module providing company app views"""
from django.http import HttpResponse


def index(request):
    """Get main page"""
    return HttpResponse(f"Main page. Request method {request.method}")
