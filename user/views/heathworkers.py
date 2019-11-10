from django.shortcuts import render, redirect
from ..forms import HealthWorkerProfileForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


def healthworker_profile_view(request):
    """
        Views that renders the HealthWorkerProfileForm for users to register as patients.
        if the form is valid and the user makes a post request, the form is saved and stored in a
        user variable.
        The user variable then calls healthworker which was declared in our models and saves it's
        value in a profile variable.
        Next we get the values fields in the form but which was only declared in the PatientProfile models
        and ensure the are validated/cleaned and then append the values to the profile variable before saving.
        if all the fields in the form does not pass validation, we render the form to the user
        """
    next = request.GET.get('next')
    if request.method == "POST":
        form = HealthWorkerProfileForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            profile = new_user.healthworker
            user_group = form.cleaned_data.get('user_type')
            phone_number = form.cleaned_data.get('phone_number')
            organization_name = form.cleaned_data.get('organization_name')
            profession = form.cleaned_data.get('profession')
            profile.user_type = user_group
            profile.phone_number = phone_number
            profile.profession = profession
            profile.organization_name = organization_name
            profile.save()
            messages.success(request, "Profile successfully created")
            return render(request, 'registration/register_done.html')
        else:
            print(HealthWorkerProfileForm.errors)
    else:
        form = HealthWorkerProfileForm()
    return render(request, 'registration/register.html', {'profile_form': form})
