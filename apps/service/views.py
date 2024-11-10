from django.shortcuts import render
from . models import Service, FeedbackClient
from django import template
from apps.package.forms import SubscriptionForm


register = template.Library()

@register.filter
def times(number):
    return range(number)

def serviceView(request):
    service1 = Service.objects.all()
    feedback_clients = FeedbackClient.objects.all()
    subs = SubscriptionForm(request.POST or None, initial={'persons': 'ONE', 'kids': 1})
    return render(request, 'services.html', {
        'service1': service1[:1],
        'service2': service1[1:],
        'feedback_clients': feedback_clients,
        "subs": subs
    })