from django.shortcuts import render

def packageView(request):
    return render(request, 'packages.html')