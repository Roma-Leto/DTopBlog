from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from .forms import TaskForm


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


class TaskFormView(FormView):
    template_name = 'blog/create.html'
    form_class = TaskForm
    success_url =reverse_lazy('profile')


