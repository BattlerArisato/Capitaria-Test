from django.shortcuts import render, redirect

# Create your views here.

def index(response):
    return render(response, 'main/index.html', {})