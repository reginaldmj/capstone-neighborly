from django.shortcuts import render
from neighborlyUsers.forms import RegisterForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from django.contrib import messages
from neighborlyUsers.models import NeighborlyUser
from django.contrib.auth.decorators import login_required


def index(request):
    form = 'index.html'
    return render(request, 'index.html')

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data['username'],
                password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('index')))
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form}) 

def logout_action(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
