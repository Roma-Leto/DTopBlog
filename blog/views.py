from django.shortcuts import render
from django.contrib.auth.views import LoginView

def index(request):
    context = {
            'text': 'Hello world'
            }
    return render(request, 'blog/index.html', context)

class BLoginView(LoginView):
    template_name = 'blog/login.html'
