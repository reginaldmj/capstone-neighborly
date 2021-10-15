from django.shortcuts import render
from neighborlyUsers.forms import NeighborlyUserChangeForm, RegisterForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from django.contrib import messages
from neighborlyUsers.models import NeighborlyUser
from posts.models import Post
from notifications.models import Notification
from django.contrib.auth.decorators import login_required
from django.views.generic import View


def error_404_view(request, exception):
    return render(request, '404.html')


def error_500(request):
    return render(request, '500.html')


class Register(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = NeighborlyUser.objects.create_user(
                username=data['username'],
                password=data['password'],
                display_name=data['display_name'],
                age=data['age'],
                email=data['email'],
            )
            return HttpResponseRedirect(reverse("login"))


class Login_View(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {"form": form})

    def post(self, request):
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


def logout_action(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def homepage_view(request):
    if request.user.is_authenticated:
        current_user = request.user
        if current_user.location:
            users = NeighborlyUser.objects.all()
            posts = Post.objects.filter(
                city=current_user.location.city).order_by('-time_stamp')
            notifications = Notification.objects.filter(user=request.user)
            notifs_count = len(notifications)
            return render(request, 'index.html', {
                "posts": posts,
                "notifications": notifications,
                "notifs_count": notifs_count,
                "users": users,
                "current_user": current_user,
            })
        else:
            return HttpResponseRedirect(reverse('location'))
    return HttpResponseRedirect(request.GET.get('next', reverse("login")))


def user_profile_view(request, id):
    html = 'profile.html'
    current_user = NeighborlyUser.objects.get(id=id)
    posts = Post.objects.filter(posted_by=current_user).order_by('-time_stamp')
    total_posts = current_user.posts
    profile_pic = current_user.profile_pic
    return render(request, html, {'posts': posts, 'total_posts': total_posts, 'profile_pic': profile_pic, "current_user": current_user})


def edit_user_view(request, id):
    current_user = NeighborlyUser.objects.get(id=id)
    if request.method == "POST":
        form = NeighborlyUserChangeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            current_user.display_name = data['display_name']
            current_user.email = data['email']
            current_user.age = data['age']
            # current_user.profile_pic = data['profile_pic']
            current_user.save()
            return HttpResponseRedirect(reverse('profile', args=(id,)))
    form = NeighborlyUserChangeForm(initial={
        'display_name': current_user.display_name,
        'email': current_user.email,
        'age': current_user.age,
        # 'profile_pic': current_user.profile_pic
    })
    return render(request, 'generic_form.html', {"form": form, "current_user": current_user})
