from django.db import models
from user.models import User
from django.urls import reverse


class HealthChallenge(models.Model):
    """
    Model for admin to add list of health challenges that a user is to select form
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Country(models.Model):
    """
    Model for admin to add list of Countries that a user is to select form
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name




class State(models.Model):
    """
    Model for admin to add list of states that a user is to select form and it has
    a foriegnkey to country which means only listed countries in the Country models can be selected
    """
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class LocalGovernment(models.Model):
    """
    Model for admin to add list of local governments that a user is to select form and it has
    a foriegnkey to country and state which means only listed countries in the Country models
    and states in the State model can be selected
    """
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class UserMedicalRecord(models.Model):
    """
    A model that will be converted to a form to allow users fill in the fields list
    in this model, many of the fields are foreignkeys to other field which means they
    are restricted to the values provided by those fields
    """
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


