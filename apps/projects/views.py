from django.shortcuts import render
from .models import Projects
# Create your views here.

def landing(request):
    projects = Projects.objects.all().order_by('position')
    context={
        'projects':projects,
    }
    return render(request, 'projects/landing.html', context)