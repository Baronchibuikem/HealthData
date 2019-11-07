from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    is_healthworker = models.BooleanField(default=False, null=True)
    is_patient = models.BooleanField(default=False, null=True)


    

class PatientProfile(models.Model):
    user_choices = (
        ('MALE', 'male'), ('FEMALE', "female"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    user_type = models.CharField(
        max_length=50, choices=user_choices, default="Male")
    phone_number = models.IntegerField(default="234", blank=False, null=False)
    location = models.CharField(max_length=30, blank=True)


    # returning a readable name to be displayed in our admin dashboard for UserProfile
    def __str__(self):
        return self.user.username



class HealthWorker(models.Model):
        # Male or Female choice where 1 and 2 and stored in MALE and FEMALE as global variable
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

	
        # returning a readable name to be displayed in our admin dashboard for UserProfile
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




