# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render_to_response, redirect, render
from unittest.mock import MagicMock
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.forms import UserCreationForm
from channel_viewer.models import Channel

class ApiClass:
	pass


def index(request: HttpRequest) -> HttpResponse:
    name = 'View Channel'
    return render_to_response('index.html', {'name': name})

def channel_posts(request, ch_name=''):
	#list = app.getUrl()
	#name = 'shved_tvoego_okna'
	#name = request.GET.get('ch_name')
	api_class = ApiClass()
	
	api_class.get_posts = MagicMock(return_value=[{'text':'Пока рассказы про то, что тут не принять на душу – не правда. В магазинах продаётся некрепкий алкоголь, а в пабах (не скажу, что их меньше, чем в Петербурге) можно выбрать из приличного ассортимента всё, что душе угодно. Только хорошее пиво стоит 100 крон (примерно 700 ₽) за пинту - особо не разгуляешься. С курильщиками ситуация такая же, как и у нас: их не то чтобы много, но они есть.', 'date':'04.05.18 15:17'},{'img':"/static/msg_images/cat.jpg",'text':'Завтра в связи с известными обстоятельствами непреодолимой силы занятий не будет. 03.05 занятий тоже не будет, поскольку у вас devdays. 10.05 будет практика вместо лекции. 17.05 и 24.05 - все в соответствии с расписанием.', 'date':'04.05.18 15:17'}, {'img':"/static/msg_images/jap.jpg",'text':'Бублик или претцель? Тест Медузы и Pomsticks о еде, которую можно есть на ходу', 'date':'04.05.18 15:17'}])
	list = api_class.get_posts()
	return render_to_response('view_posts.html', {'list': list, 'channel_name':ch_name})
	
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
	
def search(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
	    return redirect('/view_posts/'+request.POST.get('name'))  
    last_ten = Channel.objects.all().order_by('-id')[:10]
    last_ten_in_ascending_order = reversed(last_ten)
    return render_to_response('search.html', {'new_list':last_ten})
	
def create_example(request):
    t = Channel(name = 'test_channel')
    t.save()
    return render_to_response('search.html', {'new_list':last_ten})	