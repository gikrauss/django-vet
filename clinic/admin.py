from django.contrib import admin
from clinic.models import Client, Patient, MedicalRecord, Breed, Specie, Gender, Address, PhoneNumber, Vaccine


class MedicalRecordInLine(admin.TabularInline):
  model = MedicalRecord
  extra = 1

class VaccineInLine(admin.TabularInline):
  model = Vaccine
  extra = 0

class PatientAdmin(admin.ModelAdmin):
  list_display = ('name', 'owner', 'specie', 'breed')
  list_filter = ('specie', 'breed')
  inlines = [
  	MedicalRecordInLine,
    VaccineInLine,
  ]


class PhoneNumberInLine(admin.TabularInline):
  model = PhoneNumber
  extra = 0


class AddressInLine(admin.TabularInline):
  model = Address
  extra = 0


class ClientAdmin(admin.ModelAdmin):
  list_display = ('lastname', 'firstname', 'email')
  inlines = [
    PhoneNumberInLine,
    AddressInLine,
  ]


admin.site.register(Breed)
admin.site.register(Specie)
admin.site.register(Gender)

admin.site.register(Client, ClientAdmin)
admin.site.register(Patient, PatientAdmin)