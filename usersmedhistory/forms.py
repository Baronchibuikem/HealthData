from django import forms
from .models import UserMedicalRecord



class MedicalRecordForm(forms.ModelForm):
    """
    A formfield that is built from the UserMedicalRecord model in our models
    we all rendering all the fields in the model for a user to fill
    """
    class Meta:
        model = UserMedicalRecord
        fields = "__all__"

