# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render_to_response, redirect, render
from unittest.mock import MagicMock

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