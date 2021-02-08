from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .forms import NewUserForm
# Create your views here.


def index(request):
    vartotojas = User.objects.order_by('first_name')
    name_dict = {'vartotojai': vartotojas}
    return render(request, 'AppTwo/index.html', context=name_dict)


def users(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request, 'AppTwo/form_page.html', {'form': form})
