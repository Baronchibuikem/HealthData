from django.urls import path
from .views import create_medical_record, medical_record_detail, medial_history, statistics, search, access_denied, succesful

app_name = 'usersmedhistory'

urlpatterns = [
    path('', create_medical_record, name='medform'),
    path('record/<id>/', medical_record_detail, name='medrecorddetail'),
    path('medlist/', medial_history, name='medlist'),
    path('userstats/', statistics, name='stats'),
    path('successful/', succesful, name='success'),
    path('denied/', access_denied, name='permission_denied'),
    path('search/<id>/', search, name="search"),

]
