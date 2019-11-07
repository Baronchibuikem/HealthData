from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    """
    we are creating our own User model and extending from the default User model, which gives
    us access to fields already created in the default User model.

    We also add is_healthworker and is_patient to the User model which will help us different different
    users especially when creating multiple registration portal form them, this also allows us to grant access
    to any type of user we want
    """
    is_healthworker = models.BooleanField(default=False, null=True)
    is_patient = models.BooleanField(default=False, null=True)


    

class PatientProfile(models.Model):
    """
    Our application will deman that we have multiple registration portal for different user so instead of adding
    everything to our User model, we are creating this model to act as a field that will hold further fields that
    our Patient user will need to submit
    """
    user_choices = (
        ('MALE', 'male'), ('FEMALE', "female"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    user_type = models.CharField(
        max_length=50, choices=user_choices, default="Male")
    phone_number = models.IntegerField(default="234", blank=False, null=False)
    location = models.CharField(max_length=30, blank=True)


    def __str__(self):
        return self.user.username



class HealthWorker(models.Model):
    """
    Our application will deman that we have multiple registration portal for different user so instead of adding
    everything to our User model, we are creating this model to act as a field that will hold further fields that
    our HealthWorker user will need to submit
    """
    user_choices = (
        ('MALE', 'male'), ('FEMALE', "female"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    profession = models.CharField(max_length=100, blank=False)
        # fields to select a choice which has a default value of Male
    user_type = models.CharField(
        max_length=50, choices=user_choices, default="Male")
    organization_name = models.CharField(max_length=100, blank=False)
    phone_number = models.IntegerField(default="234", blank=False, null=False)


    def __str__(self):
        return self.user.username



# We create the user profile and save it to the database
@receiver(post_save, sender=User)
def create_healthworker_profile(sender, instance, created, **kwargs):
    if created:
        HealthWorker.objects.create(user=instance)
    instance.healthworker.save()



# We create the user profile and save it to the database
@receiver(post_save, sender=User)
def create_patient_profile(sender, instance, created, **kwargs):
    if created:
        PatientProfile.objects.create(user=instance)
    instance.patientprofile.save()




