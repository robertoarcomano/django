from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,
        'root.html',
        {
            'title': 'title',
            'bodystart': 'bodystart',
            'bodystop': 'bodystop',
        }
    )

