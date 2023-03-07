from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView, CreateView
from django.urls import reverse_lazy

from .forms import TaskForm
from .models import BNotePost, BUser


def index(request):
    context = {
            'text': 'Hello world'
            }
    return render(request, 'blog/index.html', context)


class BLoginView(LoginView):
    template_name = 'blog/login.html'


@login_required
def profile(request):
    btask = BNotePost.objects.all()
    extra_context = {"note": btask}
    print(extra_context)
    return render(request, 'blog/profile.html', extra_context)


class BLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'blog/logout.html'


class TaskFormView(CreateView):
    template_name = 'blog/create.html'
    form_class = TaskForm
    success_url =reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("--------------", context)
        context['user_post'] = BUser.objects.all()
        print("++++++++++++++", context['user_post'])
        return context

