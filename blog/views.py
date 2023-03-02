from django.shortcuts import render

def index(request):
    context = {
            'text': 'Hello world'
            }
    return render(request, 'index.html', context)

