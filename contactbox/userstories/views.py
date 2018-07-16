from django.shortcuts import render, redirect
from django.views import View
from .models import *
from .forms import *

# Create your views here.

def index(request):

    if request.method == "GET":
        lista_osob = Osoba.objects.all().order_by('surname')
        context = {'lista_osob':lista_osob}
        return render(request, "index.html", context)


class DodajOsobe(View):

    def get(self, request):
        form_osoba = FormOsoba()
        context = {
            'form_osoba':form_osoba,
        }
        return render(request, 'dodaj_osobe.html', context)

    def post(self, request):
        form_osoba = FormOsoba(request.POST)

        if form_osoba.is_valid():

            form_osoba.save(commit=True)

            #jak to poprawnie przekierować?
            return #redirect('userstories:osoba_info')

        else:
            print("Formularz niepoprawnie wypełniony")

        context = {
            'form_osoba': form_osoba,
        }

        return render(request, 'dodaj_osobe.html', context)


class EdytujOsobe(View):
    def get(self,request, id):
        osoba = Osoba.objects.get(id=id)
        telefony = {}
        emaile = {}

        for telefon in osoba.telefon.all():
            if telefon.phone_type == 1:
                telefony['telefon domowy'] = telefon.phone_number
            elif telefon.phone_type == 2:
                telefony['telefon służbowy'] = telefon.phone_number
            else:
                telefony['telefon komórkowy'] = telefon.phone_number

        for email in osoba.email.all():
            if email.email_type == 1:
                emaile['email prywatny'] = email.email_address
            else:
                emaile['email służbowy'] = email.email_address

        form_osoba = FormOsoba(instance=osoba)
        form_adres = FormAdres()
        form_telefon = FormTelefon()
        form_email = FormEmail()
        context = {
            'form_osoba': form_osoba,
            'form_adres':form_adres,
            'form_telefon':form_telefon,
            'form_email':form_email,
        }
        return render(request, "edytuj_osobe.html", context)

    def post(self, request, id):

        osoba = Osoba.objects.get(id=id)

        form_osoba = FormOsoba(request.POST)
        form_adres = FormAdres(request.POST)
        form_telefon = FormTelefon(request.POST)
        form_email = FormEmail(request.POST)

        if (form_osoba.is_valid and form_adres.is_valid and form_telefon.is_valid and form_email.is_valid):

            form_osoba.save(commit=True)
            form_adres.save(commit=True)
            form_telefon.save(commit=True)
            form_email.save(commit=True)

            return redirect('userstories:osoba_info', id=osoba.id)

        else:
            print("Formularz niepoprawnie wypełniony")

        context = {
            'form_osoba': form_osoba,
            'form_adres': form_adres,
            'form_telefon': form_telefon,
            'form_email': form_email,
        }

        return render(request, 'edytuj_osobe.html', context)


class OsobaInfo(View):
    def get(self, request, id):
        osoba = Osoba.objects.get(id=id)
        context = {
            'osoba':osoba
        }

        return render(request, "osoba_info.html", context)

class UsunOsobe(View):
    def get(self, request):
        return render(request, "usun_osobe.html")

class DodajGrupe(View):
    def get(self, request):
        return render(request, "dodaj_grupe.html")

class EdytujGrupe(View):
    def get(self, request):
        return render(request, "edytuj_grupe.html")

class GrupaInfo(View):
    def get(self, request):
        return render(request, "grupa_info.html")

class UsunGrupe(View):
    def get(self, request):
        return render(request, "usun_grupe.html")

class ListaGrup(View):
    def get(self, request):
        return render(request, "lista_grup.html")

class Szukaj(View):
    def get(self, request):
        return render(request, "szukaj.html")

def relative(request):
    return render(request, "relative_url_templates.html")

class Temporary(View):
    def get(self, request):
        return render(request, "temporary.html")
