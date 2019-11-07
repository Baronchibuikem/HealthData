from django.shortcuts import render, redirect
from ..forms import PatientProfileForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


def dashboard(request):
    """
    Views that renders our homepage
    """
    template = "index.html"
    return render(request, template)



def patient_profile_view(request):
    """
    Views that renders the PatientProfileForm for users to register as patients.
    if the form is valid and the user makes a post request, the form is saved and stored in a
    user variable.
    The user variable then calls patientprofile which was declared in our models and saves it's
    value in a profile variable.

    Next we get the values fields in the form but which was only declared in the PatientProfile models
    and ensure the are validated/cleaned and then append the values to the profile variable before saving.

    Next we get the values for username and password and authenticate(builtin method) them, if correct we
    log the user in and redirect to our home page

    if all the fields in the form does not pass validation, we render the form to the user
    """
    next = request.GET.get('next')
    if request.method == "POST":
        form = PatientProfileForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            profile = user.patientprofile
            user_group = form.cleaned_data.get('user_type')
            user_data = form.cleaned_data.get('user_data')
            phone_number = form.cleaned_data.get('phone_number')
            location = form.cleaned_data.get('location')
            profile.user_type = user_group
            profile.phone_number = phone_number
            profile.location = location
            profile.user_data = user_data
            profile.save()
            messages.success(request, "Profile successfully created")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            if next:
                return redirect(next)
            return render(request, "index.html")
        else:
            print(PatientProfileForm.errors)
    else:
        form = PatientProfileForm()
    return render(request, 'registration/register.html', {'profile_form': form})

