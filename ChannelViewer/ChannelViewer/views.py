# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render_to_response, redirect, render
from unittest.mock import MagicMock
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.forms import UserCreationForm
from channel_viewer.models import Channel
import ChannelViewer.TetlgBackEnd

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
    #list = ChannelViewer.TetlgBackEnd.a.getMessages(ch_name)
    print(ch_name)
    list = ChannelViewer.TetlgBackEnd.a.getMessages(ch_name)
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



print("ok")