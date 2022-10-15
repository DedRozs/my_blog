from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    
    context={}

    return render(request, 'blog/home.html', context)



def certifications(request):
    
    context={}

    return render(request, 'blog/certslanding.html', context)


def blog(request):
    
    context={}

    return render(request, 'blog/bloglanding.html', context)