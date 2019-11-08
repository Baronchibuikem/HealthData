from django.urls import path
from .views import create_medical_record, medial_history, statistics

app_name = 'usersmedhistory'


urlpatterns = [
    # this renders the create_medical_record view which is a form for users to fill
    path('', create_medical_record, name='medform'),

    # this renders the list of all our users details but is accessible to only health workers
    path('medlist/', medial_history, name='medlist'),

    # this renders a fields that show statical data of how each fields relate and a filter functionality
    path('userstats/', statistics, name='stats'),
]
