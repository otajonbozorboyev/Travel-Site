from django.shortcuts import render, redirect
from .forms import PackageForm
from .models import Package


def packageView(request):
    packages = Package.objects.all()
    form = PackageForm(request.POST or None, initial={'persons': 'ONE', 'kids': 1})
    if request.method == 'POST':
        # print("Form errors: ", form.errors)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'packages.html', {
        'packages': packages,
        'form': form,
    })
