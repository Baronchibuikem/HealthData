from django.urls import path
from user.views import heathworkers,index,patients

app_name = 'user'

urlpatterns = [
    path('', index.dashboard, name='dashboard'),
    path('healthworker/', heathworkers.healthworker_profile_view, name='healthworker'),
    path('patient/', patients.patient_profile_view, name='patient'),

]
