from django.shortcuts import render, redirect
from .models import ContactMe, Contact


def contactView(request):
    contact = ContactMe.objects.first()
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
        "contact": contact
    })