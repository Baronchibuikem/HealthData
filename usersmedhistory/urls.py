from django.urls import path
from .views import create_medical_record, medial_history, statistics, search, succesful

app_name = 'usersmedhistory'


urlpatterns = [
    # this renders the create_medical_record view which is a form for users to fill
    path('', create_medical_record, name='medform'),

    # this renders the list of all our users details but is accessible to only health workers
    path('medlist/', medial_history, name='medlist'),

    # this renders a fields that show statical data of how each fields relate
    path('userstats/', statistics, name='stats'),

    # this renders a view that shows a user (s)he's  registration was successful
    path('successful/', succesful, name='success'),

    # this is used for the filter view
    path('search/<id>/', search, name="search"),

]
