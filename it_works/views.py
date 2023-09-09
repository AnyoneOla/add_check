from django.http.response import JsonResponse
from django.shortcuts import render

def index(request):
    return render(request, 'it_works/index.html')


