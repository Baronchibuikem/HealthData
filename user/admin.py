from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import PatientProfile, HealthWorker, User




class PatientAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_type', 'location', 'phone_number']
    list_filter = ['user', 'location', 'user_type']
    search_fields = ['user', 'location']
    list_per_page = 50
admin.site.register(PatientProfile, PatientAdmin)
admin.site.register(User)

class HealthWorkerAdmin(admin.ModelAdmin):
    list_display = ['user', 'profession','user_type', 'organization_name', 'phone_number']
    list_filter = ['user', 'profession']
    search_fields = ['user', 'organization']
    list_per_page = 50
admin.site.register(HealthWorker, HealthWorkerAdmin)
