from django import forms
from . import models


class CreatePerson(forms.ModelForm):
    class Meta:
        model = models.PersonModel
        fields = ['fullname', 'job', 'email', 'domain', 'phone', 'company', 'description', 'salary', 'address']
