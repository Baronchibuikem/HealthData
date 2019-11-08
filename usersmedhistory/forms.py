from django import forms
from .models import UserMedicalRecord


class MedicalRecordForm(forms.ModelForm):
    """
    A formfield that is built from the UserMedicalRecord model in our models
    we all rendering all the fields in the model for a user to fill, the user field
    was intentionally removed to ensure it does not show up in the form, we want to ensure that
    the current logged in user is automatically detected as the current user of the form
    """
    class Meta:
        model = UserMedicalRecord
        fields = ['age', 'email', 'phone', 'country','state', 'local_government','health_challenge', 'married', 'children', 'wife', 'address', 'genotype']
