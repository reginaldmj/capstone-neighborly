from django.shortcuts import render
from neighborlyUsers.forms import RegisterForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from django.contrib import messages
from neighborlyUsers.models import NeighborlyUser
from posts.models import Post
from notifications.models import Notification
from django.contrib.auth.decorators import login_required


def error_404_view(request, exception):
    return render(request, '404.html')


def error_500(request):
    return render(request, '500.html')


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = NeighborlyUser.objects.create_user(
                username=data['username'],
                password=data['password'],
                display_name=data['display_name'],
                age=data['age'],
                email=data['email']
            )
            return HttpResponseRedirect(reverse("login"))
    form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,
                                username=data['username'],
                                password=data['password']
                                )
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("index")))
    form = LoginForm()
    return render(request, 'login.html', {"form": form})


def logout_action(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def homepage_view(request):
    if request.user.is_authenticated:
        current_user = request.user
        users = NeighborlyUser.objects.all()
        posts = Post.objects.order_by('-time_stamp')
        notifications = Notification.objects.filter(user=request.user)
        notifs_count = len(notifications)
        return render(request, 'index.html', {
            "posts": posts,
            "notifications": notifications,
            "notifs_count": notifs_count,
            "users": users,
            "current_user": current_user,
        })
    return HttpResponseRedirect(request.GET.get('next', reverse("login")))

def Profile(request, id):
    html = 'profile.html'
    user = NeighborlyUser.objects.get(id=id)
    posts = Post.objects.filter(posted_by=user).order_by('-time_stamp')
    return render(request, html, {'user': user, 'posts': posts})
