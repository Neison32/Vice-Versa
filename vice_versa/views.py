from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html')


def reverse(request):
	user_text = request.GET['reverse']
	reversed_text = user_text[::-1]
	words = user_text.split()
	words_len = len(words)
	return render(request, 'reverse.html', {'reverse':user_text,'reversedtext':reversed_text, 'words':words_len})