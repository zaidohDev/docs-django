# from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse('Ola sou a Esta é a view mais simples possível no Django!')
