from django.urls import path

from .views import signup_view

app_name = 'login'

urlpatterns = [
    # path('', ),
    path('signup', signup_view, name='signup'),
]