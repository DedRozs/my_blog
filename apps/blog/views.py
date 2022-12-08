from django.http import HttpResponse
from django.shortcuts import render
from .models import CourseraCertifications


def home(request):
    
    context={}

    return render(request, 'blog/home.html', context)



def certifications(request):
    certs = CourseraCertifications.objects.all()
    context={'certs':certs}

    return render(request, 'blog/certslanding.html', context)


def blog(request):
    
    context={}

    return render(request, 'blog/bloglanding.html', context)