#coding=utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.middleware import csrf
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def hello(request):
    return render(request, 'hello.html')