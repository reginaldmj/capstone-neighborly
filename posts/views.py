# from django.shortcuts import render, HttpResponseRedirect, reverse
# from posts.forms import AddPostForm
# from tweet.models import Tweet

# def add_post_view(request):
#     if request.user.is_authenticated:
#         current_user = request.user
#         if request.method == "POST":
#             form = AddTweetForm(request.POST)
#             users = TwitterUser.objects.all()
#             if form.is_valid():
#                 data = form.cleaned_data
#                 tweet = Tweet.objects.create(
#                     body=data['body'],
#                     user_tweeted=current_user,
#                 )
#                 current_user.tweets += 1
#                 current_user.save()
#                 for item in users:
#                     if re.search("@" + str(item), data['body']):
#                         marked = TwitterUser.objects.get(username=item)
#                         marked.notifications += 1
#                         marked.save()
#                         Notification.objects.create(
#                             tweet=Tweet.objects.get(body=data['body']),
#                             user=marked,
#                         )
#                 return HttpResponseRedirect(reverse("home"))
#         form = AddTweetForm()
#         return render(request, 'add_tweet.html', {"form": form})
#     return HttpResponseRedirect(request.GET.get('next', reverse("addtweet")))
