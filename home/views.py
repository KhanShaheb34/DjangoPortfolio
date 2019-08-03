from django.shortcuts import render
from .models import Project

# Create your views here.
def home(req):
    projects = Project.objects
    return render(req, 'home/home.html', { 'projects':projects })