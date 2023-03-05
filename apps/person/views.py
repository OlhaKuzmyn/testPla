from django.shortcuts import render, redirect
from .models import PersonModel
from django.contrib.auth.decorators import login_required
from . import forms


def persons_list(request):
    persons = PersonModel.objects.all().order_by('date')
    return render(request, 'persons_list.html', {'persons': persons})


def person_detail(request, person_id):
    person = PersonModel.objects.get(id=person_id)
    return render(request, 'person_detail.html', {{'person': person}})


@login_required(login_url="login:login")
def person_create(request):
    if request.method == 'POST':
        form = forms.CreatePerson(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('persons:persons_list')
    else:
        form = forms.CreatePerson()
    return render(request, '', {'form': form})
