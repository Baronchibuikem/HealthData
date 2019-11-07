from django.shortcuts import render
from .models import UserMedicalRecord, HealthChallenge, Country,LocalGovernment, State
from .forms import MedicalRecordForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from django.http import HttpResponseRedirect, Http404



def succesful(request):
    # this return a success page for views that need confirmation
    return render(request, "medicalrecord/success.html")

@login_required
def create_medical_record(request):
    """
    This view allows a user fill a form the MedicalRecordForm and if the form is
    valid, he is redirected to the success page else we render the form
    """
    form = MedicalRecordForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        form = MedicalRecordForm()
    template = 'medicalrecord/medicalform.html'
    context = {'form': form}
    return render(request, template, context)


def medial_history(request):
    """
    this view returns a list of all the records stored in the userMedicalRecord database,
    un-authenticated users or patient users doesn't have access to its content.
    """
    if request.user.is_anonymous or request.user.is_patient:
        return render(request, "medicalrecord/permission_denied.html")
    object = UserMedicalRecord.objects.all()
    context = {'records': object}
    template = "medicalrecord/medicalhistory.html"
    return render(request, template, context)


def statistics(request):
    queryset= UserMedicalRecord.objects.all()
    paginator = Paginator(queryset, 12)
    page_number = request.GET.get('page', 1)
    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        page = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        page = paginator.page(paginator.num_pages)

    context = {'report': page, 'page': page,}
    template = 'medicalrecord/illstatistics.html'
    return render(request, template, context)


def search(request, id):
    health = UserMedicalRecord.objects.filter(health_challenge_id=id)
    state = UserMedicalRecord.objects.filter(state_id=id)
    genotype = UserMedicalRecord.objects.filter(genotype=id)
    age = UserMedicalRecord.objects.filter(age=id)
    print(health)
    print(genotype)

    template = "medicalrecord/search.html"
    return render(request, template,)