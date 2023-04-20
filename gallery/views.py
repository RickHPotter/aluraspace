from django.shortcuts import render

template = 'gallery/'

def index(request):
    context = {
        "range" : [n for n in range(6)]
    }
    return render(request, f'{template}index.html', context)

def image(request):
    return render(request, f'{template}image.html')