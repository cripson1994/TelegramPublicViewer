# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render_to_response, redirect, render
from unittest.mock import MagicMock
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

class ApiClass:
	pass


def index(request: HttpRequest) -> HttpResponse:
    name = 'View Channel'
    return render_to_response('index.html', {'name': name})

def channel_posts(request: HttpRequest) -> HttpResponse:
	#list = app.getUrl()
	api_class = ApiClass()
	api_class.get_posts = MagicMock(return_value=['Бублик или претцель? Тест Медузы и Pomsticks о еде, которую можно есть на ходу'])
	list = api_class.get_posts()
	return render_to_response('view_posts.html', {'list': list})
	
def login(request: HttpRequest) -> HttpResponse:
    return render_to_response('signin.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})