from django import forms
from .models import UserMedicalRecord, HealthChallenge, Country

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = UserMedicalRecord
        # fields = ['age','email','phone','diabetic','hiv_infested','ebola',
        #           'genotype','married','address','state', 'country', 'general']
        fields = "__all__"

class Country(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'