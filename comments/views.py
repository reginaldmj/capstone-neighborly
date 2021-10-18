from .models import Comment
from .forms import CommentForm
from django.shortcuts import render, HttpResponseRedirect, redirect, reverse
from posts.models import Post


def create_comment_view(request, id):
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=post).order_by("-id")
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_comment = Comment.objects.create(
                post=post,
                body=data['body'],
                posted_by=request.user,
            )
            post.comment_count += 1
            post.save()
            return HttpResponseRedirect(reverse('index'))
    form = CommentForm()
    return render(request, 'generic_form.html', {'form': form})
