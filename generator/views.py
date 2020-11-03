from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
	return render(request, 'generator/home.html')

def password(request):

	characters = list('abcedfghijklmnopqrstuvwxyz')
	mPassword = ''

	if request.GET.get('uppercase'):
		characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

	if request.GET.get('special'):
		characters.extend(list('!@#$*()_^&'))

	if request.GET.get('number'):
		characters.extend(list('0123456789'))

	length = int(request.GET.get('length', 12))
	for x in range(length):
		mPassword += random.choice(characters)

	return render(request, 'generator/password.html', {'password': mPassword})

def about(request):
	return render(request, 'generator/about.html')