from django.shortcuts import render

def contactView(request):
    return render(request, 'contact.html')