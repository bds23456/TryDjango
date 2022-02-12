from django.shortcuts import render
from django.http import HttpResponse


def index(requests):
    return render(requests, 'main/index.html')


def but(requests):
    return render(requests, 'main/button.html')
