from django.contrib import admin
from .models import billheader, billdetails, billreceipt, patient_registration, PrescriptionMedication, PrescriptionHeader
# Register your models here.

admin.site.register((billheader, billdetails, billreceipt, patient_registration, PrescriptionMedication, PrescriptionHeader))
