from .models import Comment
from .forms import CommentForm
from django.shortcuts import render, HttpResponseRedirect, redirect, reverse
from posts.models import Post
 
def com_detailview(request, id):
  post = Post.objects.get(id=id)
  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      comment = Comment.objects.create(
        content = data['content'],
        user = request.user,
        image = data['image']
      )
    
      return HttpResponseRedirect(reverse('index'))
       
   
  form = CommentForm()
  return render(request, 'generic_form.html', {'form':form,})
