from django.contrib import admin
from .models import UserMedicalRecord, HealthChallenge, Country,State


class UserMedicalRecordAdmin(admin.ModelAdmin):
    list_display = ['user', 'age', 'email', 'phone',
                    'married',  'genotype', 'health_challenge',"health_status", 'state','country']
    list_filter = ['genotype', 'married','health_challenge',"health_status", 'state','country']
    search_fields = ['user', 'email']
    list_per_page = 50


class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    list_filter = ['name',]
    list_per_page = 50
    search_fields = ['name',]


class StateAdmin(admin.ModelAdmin):
    list_display = ['name', 'country' ]
    list_filter = ['name', 'country']
    list_per_page = 50
    search_fields = ['name',]

class HealthChallengeAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    list_per_page = 50


admin.site.register(HealthChallenge, HealthChallengeAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(UserMedicalRecord, UserMedicalRecordAdmin)