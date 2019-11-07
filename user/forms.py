from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User



class PatientProfileForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True, help_text="Please enter your first name")
    last_name = forms.CharField(max_length=50, required=True, help_text="Please enter your last name")
    email = forms.EmailField(max_length=300, required=True, help_text="Please input a valid email address")
    user_types =  (("MALE", "male"), ("FEMALE", "female"))
    user_type = forms.ChoiceField(choices=user_types)
    phone_number = forms.IntegerField(required=True)
    location = forms.CharField(max_length=100, required=True)
    is_patient = forms.BooleanField(disabled=True, initial=True)

    class Meta:
        model = User
        fields = ("username", 'first_name', 'last_name', 'email','user_type', 'phone_number', 'location' ,'password1', 'password2')


class HealthWorkerProfileForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True, help_text="Please enter your first name")
    last_name = forms.CharField(max_length=50, required=True, help_text="Please enter your last name")
    email = forms.EmailField(max_length=300, required=True, help_text="Please input a valid email address")
    user_types =  (("MALE", "male"), ("FEMALE", "female"))
    user_type = forms.ChoiceField(choices=user_types)
    phone_number = forms.IntegerField(required=True)
    profession = forms.CharField(max_length=50)
    organization_name = forms.CharField(max_length=100)
    is_healthworker = forms.BooleanField(disabled=True, initial=True)

    class Meta:
        model = User
        fields = ("username", 'first_name', 'last_name', 'email','user_type', 'is_healthworker','organization_name', 'profession', 'phone_number','password1', 'password2')
