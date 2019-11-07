from django.shortcuts import render, redirect
from ..forms import PatientProfileForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


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
            profile = user.patientprofile
            # We get all the validated data in our form.(you can add more custom fields here)
            user_group = form.cleaned_data.get('user_type')
            user_data = form.cleaned_data.get('user_data')
            phone_number = form.cleaned_data.get('phone_number')
            location = form.cleaned_data.get('location')
            # each of the cleaned data is updated to our profile instances
            profile.user_type = user_group
            profile.phone_number = phone_number
            profile.location = location
            profile.user_data = user_data
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

