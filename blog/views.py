from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    context = {
            'text': 'Hello world'
            }
    return render(request, 'blog/index.html', context)


class BLoginView(LoginView):
    template_name = 'blog/login.html'


@login_required
def profile(request):
    return render(request, 'blog/profile.html')


class BLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'blog/logout.html'

