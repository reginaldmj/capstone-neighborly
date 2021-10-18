from django.views.generic import DetailView
from django.shortcuts import render, HttpResponseRedirect, reverse
from posts.forms import PostForm
from posts.models import Post
from notifications.models import Notification
from neighborlyUsers.models import NeighborlyUser
import re
from django.views.generic import View
from comments.models import Comment


class Post_Detail_View(View):

    def get(self, request, id):
        current_user = request.user
        posts = Post.objects.all()
        post = Post.objects.get(id=id)
        comments = Comment.objects.filter(post=post).order_by("-id")
        template_name = "post.html"
        is_admin = request.user.is_superuser
        context = {"post": post, "current_user": current_user,
                   "is_admin": is_admin, "posts": posts, 'comments': comments}
        return render(request, template_name, context)


def add_post_view(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES)
            users = NeighborlyUser.objects.all()
            if form.is_valid():
                data = form.cleaned_data
                post = Post.objects.create(
                    title=data['title'],
                    body=data['body'],
                    image=data['image'],
                    posted_by=current_user,
                    city=current_user.location.city
                )
                current_user.posts += 1
                current_user.save()
                for item in users:
                    if re.search("@" + str(item), data['body']):
                        marked = NeighborlyUser.objects.get(username=item)
                        marked.notifications += 1
                        marked.save()
                        Notification.objects.create(
                            post=Post.objects.get(body=data['body']),
                            user=marked,
                        )
                return HttpResponseRedirect(reverse("index"))
        form = PostForm()
        return render(request, 'generic_form.html', {"form": form})
    return HttpResponseRedirect(request.GET.get('next', reverse("addpost")))


def edit_post_view(request, id):
    post = Post.objects.get(id=id)
    current_user = request.user
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if data['image']:
                post.image = None
                post.image = data['image']
            post.title = data['title']
            post.body = data['body']
            post.save()
            return HttpResponseRedirect(reverse('post', args=(id,)))
    form = PostForm(initial={
        'title': post.title,
        'body': post.body,
        'image': post.image,
    })
    return render(request, 'generic_form.html', {"form": form, "current_user": current_user})


def delete_post_view(request, id):
    post_to_delete = Post.objects.get(id=id)
    post_to_delete.delete()
    request.user.posts -= 1
    request.user.save()
    return HttpResponseRedirect(reverse("index"))
