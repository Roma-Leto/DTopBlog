from django.contrib import admin
from django.urls import path
from blog.views import index, BLoginView, profile, BLogoutView, user_task_add, \
        RegisterUserView, RegisterDoneView

urlpatterns = [
        path('accounts/register/done', RegisterDoneView.as_view(), name'register_done')
        path('accounts/register/', RegisterUserView.as_view(), name'register')
        path('accounts/create/', user_task_add, name='create'),
        path('accounts/logout', BLogoutView.as_view(), name='logout'),
        path('accounts/profile/', profile, name='profile'),
        path('accounts/login/', BLoginView.as_view(), name='login'),
        path('', index, name='index'),
        path('admin/', admin.site.urls),
    ]
