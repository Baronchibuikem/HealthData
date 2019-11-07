from django.shortcuts import render, redirect
from .forms import PatientProfileForm, HealthWorkerProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User, PatientProfile, HealthWorkerProfile
from django.http import HttpResponseRedirect


def dashboard(request):
    template = "index.html"
    return render(request, template, {})


# For user registration
def patient_profile_view(request):
    next = request.GET.get('next')
    # if the method is POST, we render the form to the user and
    # if the form inputs are all valid,
    if request.method == "POST":
        form = PatientProfileForm(data=request.POST)
        if form.is_valid():
            # we save the form and store it in a user variable for further processing
            user = form.save()
            # we call the instance of our userprofile which was declared in our models and saved
            # it to a profile variable
            profile = user
            # We get all the validated data in our form.(you can add more custom fields here)
            user_group = form.cleaned_data.get('user_type')
            phone_number = form.cleaned_data.get('phone_number')
            location = form.cleaned_data.get('location')
            # each of the cleaned data is updated to our profile instances
            profile.user_type = user_group
            profile.phone_number = phone_number
            profile.location = location
            # we save the user profile which is then stored in our database
            profile.save()
            # if successfully saved, we return a message that the profile was successfully created
            messages.success(request, "Profile successfully created")
            # we get the cleaned data inputs from our form for username and password
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # authenticate and ensure the are valid while storing the values in a user variable
            user = authenticate(username=username, password=password)
            # we call the built in django login functionality and pass request and the authenticate user
            login(request, user)
            #if successful, we render a register_done/success page
            if next:
                return redirect(next)
            return render(request, "index.html")
        # we print out the errors
        else:
            print(PatientProfileForm.errors)
    # else we render the form if the fields are not valid
    else:
        form = PatientProfileForm()
    return render(request, 'registration/register.html', {'profile_form': form})




# For user registration
def healthworker_profile_view(request):
    next = request.GET.get('next')
    # if the method is POST, we render the form to the user and
    # if the form inputs are all valid,
    if request.method == "POST":
        form = HealthWorkerProfileForm(data=request.POST)
        if form.is_valid():
            # we save the form and store it in a user variable for further processing
            user = form.save()
            # we call the instance of our userprofile which was declared in our models and saved
            # it to a profile variable
            profile = user
            # We get all the validated data in our form.(you can add more custom fields here
            user_group = form.cleaned_data.get('user_type')
            phone_number = form.cleaned_data.get('phone_number')
            organization_name = form.cleaned_data.get('organization_name')
            profession = form.cleaned_data.get('profession')
            # each of the cleaned data is updated to our profile instances
            profile.user_type = user_group
            profile.phone_number = phone_number
            profile.profession = profession
            profile.organization_name = organization_name
            # we save the user profile which is then stored in our database
            profile.save()
            # if successfully saved, we return a message that the profile was successfully created
            messages.success(request, "Profile successfully created")
            # we get the cleaned data inputs from our form for username and password
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # authenticate and ensure the are valid while storing the values in a user variable
            user = authenticate(username=username, password=password)
            # we call the built in django login functionality and pass request and the authenticate user
            login(request, user)
            #if successful, we render a register_done/success page
            if next:
                return redirect(next)
            return render(request, "registration/register_done.html")
        # we print out the errors
        else:
            print(HealthWorkerProfileForm.errors)
    # else we render the form if the fields are not valid
    else:
        form = HealthWorkerProfileForm()
    return render(request, 'registration/register.html', {'profile_form': form})
