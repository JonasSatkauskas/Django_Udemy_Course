from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.

def index(request):
    vartotojas = User.objects.order_by('first_name')
    name_dict = {'vartotojai': vartotojas}
    return render(request, 'AppTwo/index.html', context=name_dict)