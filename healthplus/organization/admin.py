from django.contrib import admin
from organization.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Organization)
admin.site.register(OrganizationUser)
admin.site.register(Patient)
admin.site.register(Doctor)
