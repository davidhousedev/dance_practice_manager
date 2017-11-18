from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse(f'Hello, {request.GET.get("name")}')