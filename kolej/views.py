from django.shortcuts import render

# Create your views here.
from .models import Teacher

def index(request):
    teacher=Teacher.objects.all()
    return render(request, 'base.html',{'teacher':teacher})
def prof(request):
    teacher=Teacher.objects.all()
    return render(request, 'prof.html',{'teacher':teacher})