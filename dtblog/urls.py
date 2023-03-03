from django.contrib import admin
from django.urls import path
from blog.views import index, BLoginView


urlpatterns = [
    path('accounts/login/', BLoginView.as_view(), name='login'),
    path('', index, name='index'),
    path('admin/', admin.site.urls),
]
