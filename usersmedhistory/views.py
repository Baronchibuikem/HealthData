from django.shortcuts import render
from .models import UserMedicalRecord, HealthChallenge, Country, LocalGovernment, State
from .forms import MedicalRecordForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q, Count
from django.http import JsonResponse


@login_required
def create_medical_record(request):
    """
    This view allows a user fill a form the MedicalRecordForm and if the form is
    valid, he is redirected to the success page else we render the form
    """
    form = MedicalRecordForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Successfully Created")
        return render(request, "medicalrecord/success.html")
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
    queryset = UserMedicalRecord.objects.all()

    # For filtering out genotypes
    genotype = request.GET.get('genotype')
    if genotype != '' and genotype is not None:
        queryset = queryset.filter(genotype__icontains=genotype)

    # For filtering out states
    state = request.GET.get('state')
    if state != '' and state is not None:
        queryset = queryset.filter(state__name__icontains=state)

    # for filtering out health challenges
    health = request.GET.get('health')
    if health != '' and health is not None:
        queryset = queryset.filter(health_challenge__name__icontains=health)

    # for filtering out country
    country = request.GET.get('country')
    if country != '' and country is not None:
        queryset = queryset.filter(country__name__icontains=country)

    # for pagination
    paginator = Paginator(queryset, 30)
    page_number = request.GET.get('page', 1)
    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        page = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        page = paginator.page(paginator.num_pages)

    context = {"queryset": queryset, 'page': page, }
    template = 'medicalrecord/illstatistics.html'
    return render(request, template, context)


def age_type_view(request):
    # dataset = UserMedicalRecord.objects.values('age').annotate(married_count=Count('age', filter=Q(married=True)),
    #  not_married_count=Count('age', filter=Q(married=False))).order_by('age')
    # print(dataset)
    # return render(request, 'charts.html', {'dataset': dataset})
    # genotype = UserMedicalRecord.objects.values("genotype")
    # print(genotype)
    dataset = UserMedicalRecord.objects.values("genotype")\
                .exclude(genotype="")\
                .annotate(total=Count("genotype"))\
                .order_by("genotype")

    genotype_name = dict()
    print(genotype_name)
    for genotype_tuple in UserMedicalRecord.user_choices:
        genotype_name[genotype_tuple[0]] = genotype_tuple[1]

    chart = {
        "chart": {"type": "pie"},
        "title": {"text": "Genotypes prone to more health Challenges"},
        "series": [{
            "name": "Number of Patients",
            "data": list(map(lambda row: {"name": genotype_name[row["genotype"]],
                                          "y":row["total"]}, dataset))
        }]
    }
    print(chart)
    return JsonResponse(chart)
