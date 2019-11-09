from django.urls import path
from .views import create_medical_record, medial_history, statistics, chart_view, condition_status_view

app_name = 'usersmedhistory'


urlpatterns = [
    # this renders the create_medical_record view which is a form for users to fill
    path('', create_medical_record, name='medform'),

    # this renders the list of all our users details but is accessible to only health workers
    path('medlist/', medial_history, name='medlist'),

    # this renders a fields that show statical data of how each fields relate and a filter functionality
    path('userstats/', statistics, name='stats'),

    # this points to the view that renders our genotype chart
    path('chart/', chart_view, name='chart_data'),

    # this points to the view that renders our contagious and non_contagious chart
    path('condition/', condition_status_view, name='condition_data'),
]
