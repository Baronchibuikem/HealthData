from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('medhistory/', include('usersmedhistory.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
