from django.db import models
from user.models import User
from django.urls import reverse
from django.db.models import Sum



class HealthChallenge(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class LocalGovernment(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class UserMedicalRecord(models.Model):
    user_choices = (
        ('AA', 'AA'), ('AS', "AS"),('SS', 'SS')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    phone = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    local_government = models.ForeignKey(LocalGovernment, on_delete=models.CASCADE)
    health_challenge = models.ForeignKey(HealthChallenge, on_delete=models.CASCADE)
    married = models.BooleanField(default=False)
    children = models.IntegerField()
    wife = models.IntegerField
    address = models.CharField(max_length=250)
    genotype = models.CharField(max_length=2, choices=user_choices)
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["user"]

    def __str__(self):
        return self.user.username


    def get_absolute_url(self):
        return reverse('usersmedhistory:medrecorddetail',
                       args=[self.id])
