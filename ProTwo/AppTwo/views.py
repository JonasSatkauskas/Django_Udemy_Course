from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from . import forms
# Create your views here.

def index(request):
    vartotojas = User.objects.order_by('first_name')
    name_dict = {'vartotojai': vartotojas}
    return render(request, 'AppTwo/index.html', context=name_dict)


def user_form_view(request):
    form = forms.FormUser()
    return render(request, 'AppTwo/form_page.html', {'form': form})