from django.shortcuts import render, redirect
from apps.about.models import About, Guide
from apps.service.models import Service, FeedbackClient
from django.db.models import Count
from apps.pages.models import TourCategory, OurCategory, Destination, Gallery
from apps.package.models import Package
from apps.package.forms import PackageForm, SubscriptionForm
from apps.blog.models import Blog


def indexView(request):
    about = About.objects.all()
    service1 = Service.objects.all()
    destination = Destination.objects.prefetch_related('images').select_related('ctg')
    packages = Package.objects.all()
    gallery_ctg = OurCategory.objects.filter(status=True)
    gallery = Gallery.objects.prefetch_related('images').select_related('ctg')
    form = PackageForm(request.POST or None, initial={'persons': 'ONE', 'kids': 1})
    if request.method == 'POST':
        print("Form errors: ", form.errors)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    guide = Guide.objects.all().order_by('-id')[:5]
    blog = Blog.objects.all().order_by('-id')
    feedback_clients = FeedbackClient.objects.all()
    subs = SubscriptionForm(request.POST or None, initial={'persons': 'ONE', 'kids': 1})
    

    return render(request, 'index.html', context={
        'abouts': about,
        'service1': service1[:1],
        'service2': service1[1:],
        'destination': destination.annotate(destination_num=Count('images')),
        "tour_category": TourCategory.objects.all(),
        'gallery_ctg': gallery_ctg,
        'gallery': gallery,
        'packages': packages,
        'form': form,
        'guides': guide,
        'blogs': blog,
        'feedback_clients': feedback_clients,
        "subs": subs
    })