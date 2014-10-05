from django.contrib import admin
from core.models import Client, Patient, MedicalRecord, Breed, Specie, Gender 


class MedicalRecordInLine(admin.TabularInline):
	model = MedicalRecord
	extra = 1


class PatientAdmin(admin.ModelAdmin):
  list_display = ('name', 'owner', 'specie', 'breed')
  list_filter = ('specie', 'breed')
  inlines = [
  	MedicalRecordInLine,
  ]



admin.site.register(Breed)
admin.site.register(Specie)
admin.site.register(Gender)

admin.site.register(Client)
admin.site.register(Patient, PatientAdmin)
