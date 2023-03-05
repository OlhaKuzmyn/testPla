from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class PersonModel(models.Model):
    class Meta:
        db_table = 'person'
        ordering = ['date']

    fullname = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    email = models.EmailField()
    domain = models.URLField(max_length=500, blank=True)
    phone = models.IntegerField(blank=True)
    company = models.CharField(max_length=200, blank=True)
    description = models.TextField(max_length=3000, blank=True)
    salary = models.IntegerField(validators=[MinValueValidator(1000), MaxValueValidator(1000000)], blank=True)
    address = models.CharField(max_length=200, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='persons')
