from django.shortcuts import render, redirect
from .models import ContactMe, Contact
from apps.package.forms import SubscriptionForm


def contactView(request):
    contact = ContactMe.objects.first()
    subs = SubscriptionForm(request.POST or None, initial={'persons': 'ONE', 'kids': 1})
    if request.method == 'POST':
        data = request.POST
        Contact.objects.create(
            full_name=data.get('name'),
            email=data.get('email'),
            subject=data.get('subject'),
            message=data.get('msg')
        )
        return redirect('contact')
    
    return render(request, 'contact.html', context={
        "contact": contact,
        "subs": subs
    })