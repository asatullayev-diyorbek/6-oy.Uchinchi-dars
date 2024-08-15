from django.shortcuts import render
from django.shortcuts import redirect


def index(request):
    context = {
        'title': 'Bosh sahifa'
    }
    return render(request, 'index.html', context)

