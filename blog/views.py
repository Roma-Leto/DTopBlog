from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect

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


@login_required
def user_task_add(request):
    request.user_post_id=request.user.pk
    print("---REQUEST---", request.method)
    if request.method != 'GET':
        form = TaskForm(request.POST)
        print("---FORM---", form)
        if form.is_valid():
            task = form.save()
            if formset.is_valid():
               formset.save()
               messages.add_message(request, messages.SUCCESS,
                                     'Задача добавлена')
               return redirect('profile')
    else:
        form = TaskForm(initial={'user_post_id': request.user.pk})
    context = {'form': form}
    return render(request, 'blog/create.html', context)

