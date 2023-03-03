from django.contrib import admin
from django.urls import path
from blog.views import index, BLoginView, profile


urlpatterns = [
        path('accounts/logout', BLogoutView.as_view(), name='logout'),
        path('accounts/profile/', profile, name='profile'),
        path('accounts/login/', BLoginView.as_view(), name='login'),
        path('', index, name='index'),
        path('admin/', admin.site.urls),
]
