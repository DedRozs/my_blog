from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render

  
def home(request):
    context={}
    return render(request,"blog/home.html", context)