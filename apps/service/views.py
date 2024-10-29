from django.shortcuts import render


def serviceView(request):
    return render(request, 'services.html')