from django.shortcuts import render

# Create your views here.


def pasveikinimas(request):
    my_dict = {'pasveikinimas_tag': '   Kas geresnio?'}
    return render(request, 'AppFour/index.html', context=my_dict)