from django.shortcuts import render
from .models import Blog
from apps.package.forms import SubscriptionForm


def blogView(request):
    subs = SubscriptionForm(request.POST or None, initial={'persons': 'ONE', 'kids': 1})
    blog = Blog.objects.all().order_by('-id')
    return render(request, 'blog.html', {
        'blogs': blog,
        "subs": subs,

    })
