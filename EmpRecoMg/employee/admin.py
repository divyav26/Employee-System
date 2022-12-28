from django.contrib import admin
from .models import EmployeeDetails,EmployeeEduction,EmployeeExperience
# Register your models here.

admin.site.register(EmployeeDetails)
admin.site.register(EmployeeEduction)
admin.site.register(EmployeeExperience)