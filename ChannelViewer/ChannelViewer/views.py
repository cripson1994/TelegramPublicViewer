# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render_to_response, redirect, render


def index(request: HttpRequest) -> HttpResponse:
    name = 'View Channel'
    return render_to_response('index.html', {'name': name})

def sign_in(request: HttpRequest) -> HttpResponse:
    return render_to_response('signin.html')