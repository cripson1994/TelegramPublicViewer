# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render_to_response, redirect, render
from unittest.mock import MagicMock
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.forms import UserCreationForm

class ApiClass:
	pass


def index(request: HttpRequest) -> HttpResponse:
    name = 'View Channel'
    return render_to_response('index.html', {'name': name})

def channel_posts(request: HttpRequest) -> HttpResponse:
	#list = app.getUrl()
	name = 'Юмор от Влада @Vlad_MDK'
	api_class = ApiClass()
	
	api_class.get_posts = MagicMock(return_value=[{'img':"/static/msg_images/cat.jpg",'text':'Завтра в связи с известными обстоятельствами непреодолимой силы занятий не будет. 03.05 занятий тоже не будет, поскольку у вас devdays. 10.05 будет практика вместо лекции. 17.05 и 24.05 - все в соответствии с расписанием.', 'date':'04.05.18 15:17'}, {'img':"/static/msg_images/jap.jpg",'text':'Бублик или претцель? Тест Медузы и Pomsticks о еде, которую можно есть на ходу', 'date':'04.05.18 15:17'}])
	list = api_class.get_posts()
	return render_to_response('view_posts.html', {'list': list, 'channel_name':name})
	
def login(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        #form = UserLoginForm(request.POST)
        username = request.POST.get('username', '')
        print(username)
        password = request.POST.get('password', '')
        print(password)
        user = authenticate(username=username, password=password)
        if user is not None:
            return redirect('/view_posts')
        else:
            return redirect('/')

    return render_to_response('signin.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            #login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
	
