from django.contrib import admin
from core.models import Client, Patient, Breed, Specie, Gender 

admin.site.register(Client)
admin.site.register(Patient)
admin.site.register(Breed)
admin.site.register(Specie)
admin.site.register(Gender)

