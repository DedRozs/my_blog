from django.contrib import admin
from .models import Skills, AwardingInstitutions, CourseraCertifications

# Register your models here.

admin.site.register(Skills)
admin.site.register(AwardingInstitutions)
admin.site.register(CourseraCertifications)