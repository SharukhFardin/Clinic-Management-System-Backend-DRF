from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Appointment)
admin.site.register(LabTest)
admin.site.register(Medicine)
admin.site.register(MedicineCategory)
admin.site.register(Disease)
admin.site.register(DiseaseCategory)
admin.site.register(LabTestAppointmentConnector)
