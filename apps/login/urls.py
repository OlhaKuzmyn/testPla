from django.urls import path

from .views import signup_view, login_view

app_name = 'login'

urlpatterns = [
    path('', login_view, name='login'),
    path('signup', signup_view, name='signup'),
]