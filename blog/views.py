from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView, CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect


from .forms import RegisterUserForm


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
    return render(request, 'blog/profile.html', extra_context)


class BLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'blog/logout.html'


@login_required
def user_task_add(request):
    request.user_post=request.user.pk
    #print("---REQUEST---", request.method, 'user_id=', request.user_post)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        #print("---FORM---", form)
        if form.is_valid():
            #form = TaskForm(initial={'user_post': request.user.pk})
            #user_post_id=request.user.pk
            #print('--- PRINT VALID ---', form, request.body)
            task = form.save()
            print('--- TASK ---', task)
            return redirect('index')
    else:
        #form = TaskForm()
        form = TaskForm(initial={'user_post': request.user.pk})
        #print('---form initial---', form)
        context = {'form': form}
        #print('---request---', context)
        return render(request, 'blog/create.html', context)
    return render(request, 'blog/create.html', {'form': form})


class RegisterUserView(CreateView):
    model = BUser
    template_name = 'blog/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('blog:register_done')


class RegisterDoneView(TemplateView):
    tamplate_name = 'blog/index.html'

