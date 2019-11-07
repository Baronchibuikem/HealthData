from django.contrib import admin
from .models import UserMedicalRecord, HealthChallenge, Country, LocalGovernment, State


class UserMedicalRecordAdmin(admin.ModelAdmin):
    list_display = ['user', 'age', 'email', 'phone',
                    'married', 'children', 'genotype', 'wife', 'address','country']
    list_filter = ['user', 'age', 'married']
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

class LocalGovernmentAdmin(admin.ModelAdmin):
    list_display = ['name','country','state' ]
    list_filter = ['name', 'country','state' ]
    list_per_page = 50
    search_fields = ['name','country','state'  ]

class HealthChallengeAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    list_per_page = 50


admin.site.register(HealthChallenge, HealthChallengeAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(LocalGovernment, LocalGovernmentAdmin)
admin.site.register(UserMedicalRecord, UserMedicalRecordAdmin)