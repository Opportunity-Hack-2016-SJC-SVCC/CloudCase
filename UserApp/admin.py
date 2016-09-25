from django.contrib import admin

# Register your models here.
from django.contrib import admin

from UserApp.models import CaseOfficer


class CaseOfficerAdmin(admin.ModelAdmin):
    pass

admin.site.register(CaseOfficer, CaseOfficerAdmin)