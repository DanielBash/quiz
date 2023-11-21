from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def mainpage(request):
    context = {'title': 'Тест'}
    return render(request, 'mainpage/index.html', context=context)