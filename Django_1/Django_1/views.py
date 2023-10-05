from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return HttpResponse('This is my home')

def home(request):
    return render(request, 'home.html')

def reverse(request):
    user_text = request.GET['user']
    reverse = user_text[::-1]
    return render(request, 'reverse.html', {'word': reverse})