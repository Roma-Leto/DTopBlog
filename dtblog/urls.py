from django.contrib import admin
from django.urls import path
from blog.views import index, BLoginView, profile, BLogoutView, TaskFormView

urlpatterns = [
	path('accounts/create/', TaskFormView.as_view(), name='create'),
        path('accounts/logout', BLogoutView.as_view(), name='logout'),
        path('accounts/profile/', profile, name='profile'),
        path('accounts/login/', BLoginView.as_view(), name='login'),
        path('', index, name='index'),
        path('admin/', admin.site.urls),
]
