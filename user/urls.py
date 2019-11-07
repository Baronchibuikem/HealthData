from django.urls import path
from user.views import heathworkers,index,patients

app_name = 'user'

urlpatterns = [
    # For the home page
    path('', index.dashboard, name='dashboard'),

    # for health worker registration
    path('healthworker/', heathworkers.healthworker_profile_view, name='healthworker'),

    # for patient registration
    path('patient/', patients.patient_profile_view, name='patient'),
]
