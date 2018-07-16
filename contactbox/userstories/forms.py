from django import forms
from userstories.models import Adres, Osoba, Telefon, Email, Grupy, PHONE_CHOICES, EMAIL_CHOICES


class FormAdres(forms.ModelForm):
    class Meta():
        model = Adres
        fields = "__all__"

class FormOsoba(forms.ModelForm):
    class Meta():
        model = Osoba
        exclude = ('adres',)

class FormTelefon(forms.ModelForm):
    class Meta():
        model = Telefon
        exclude = ('osoba',)

class FormEmail(forms.ModelForm):
    class Meta():
        model = Email
        exclude = ('osoba',)

class FormGrupy(forms.ModelForm):
    class Meta():
        model = Grupy
        exclude = ('osoby',)



