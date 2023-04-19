from django.shortcuts import render

template = 'gallery/'

def index(request):
    return render(request, f'{template}index.html')

def image(request):
    return render(request, f'{template}image.html')