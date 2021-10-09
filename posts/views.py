from django.views.generic import DetailView
from django.shortcuts import render, HttpResponseRedirect, reverse
from posts.forms import AddPostForm
from posts.models import Post
from neighborlyUsers.models import NeighborlyUser
import re
from django.db.models import Count

def add_post_view(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == "POST":
            form = AddPostForm(request.POST, request.FILES)
            users = NeighborlyUser.objects.all()
            if form.is_valid():
                data = form.cleaned_data
                post = Post.objects.create(
                    body=data['body'],
                    image=data['image'],
                    posted_by=current_user,
                )
                current_user.posts += 1
                current_user.save()
                # for item in users:
                #     if re.search("@" + str(item), data['body']):
                #         marked = NeighborlyUser.objects.get(username=item)
                #         marked.notifications += 1
                #         marked.save()
                #         Notification.objects.create(
                #             post=Post.objects.get(body=data['body']),
                #             user=marked,
                #         )
                return HttpResponseRedirect(reverse("index"))
        form = AddPostForm()
        return render(request, 'generic_form.html', {"form": form})
    return HttpResponseRedirect(request.GET.get('next', reverse("addpost")))


def Post_View(request, id):
    html = "posts.html"
    post = Post.objects.get(id=id)
    likes = post.likes.count()
    return render(request, html, {'post': post, 'likes': likes, })

def like(request, post_id):
    posts = Post.objects.get(id=post_id)
    posts.likes.add(request.user)
    posts.save()
    return HttpResponseRedirect(reverse('index'))

def dislike(request, post_id):
    posts = Post.objects.get(id=post_id)
    posts.likes.remove(request.user)
    posts.save()
    return HttpResponseRedirect(reverse('index'))