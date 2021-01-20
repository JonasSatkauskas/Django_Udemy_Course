from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<em>My Third App</em>')


def help(request):
    my_dict = {'insert_tag': ''}
    return render(request, 'AppThree/index.html', context=my_dict)