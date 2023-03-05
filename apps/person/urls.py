from django.urls import path

from .views import persons_list, person_detail, person_create

app_name = 'persons'

urlpatterns = [
    path('', persons_list, name='persons_list'),
    path('/<int:person_id>', person_detail, name='detail'),
    path('/create', person_create, name='create'),

]