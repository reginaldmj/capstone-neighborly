from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from neighborlyUsers.models import NeighborlyUser
from notifications.models import Notification


@login_required
def notification_view(request, id):
    if request.user.is_authenticated:
        user = NeighborlyUser.objects.get(id=id)
        notifications = Notification.objects.filter(user=request.user)
        copy_posts = [post for post in notifications]
        Notification.objects.filter(user=request.user).delete()

        return render(request, "notifications.html", {
            "user": user,
            "notifications": copy_posts
        })
    return HttpResponseRedirect(reverse("login"))
