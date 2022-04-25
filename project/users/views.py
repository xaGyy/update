from django.contrib.auth import authenticate, login
from django.views import View
from django.shortcuts import render, redirect

from .models import Mobile
from .forms import MobileForm

from users.forms import UserCreationForm


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


def create(request):
    error = ''
    if request.method == 'POST':
        form = MobileForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('home')
        else:
            error = 'Форма была неверной'

    form = MobileForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'create.html')