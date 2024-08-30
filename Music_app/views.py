from django.shortcuts import render
from .models import Music
# Create your views here.

def index(request):
    music = Music.objects.order_by('nome')
    context = {'music':music}
    return render(request, 'index.html',context)