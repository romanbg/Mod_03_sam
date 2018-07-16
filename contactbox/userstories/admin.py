from django.contrib import admin
from userstories.models import Adres, Osoba, Telefon, Email, Grupy

# Register your models here.

admin.site.register(Adres)
admin.site.register(Osoba)
admin.site.register(Telefon)
admin.site.register(Email)
admin.site.register(Grupy)
