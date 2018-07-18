from django.shortcuts import render, redirect, render_to_response
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
        form_grupa = FormGrupy()
        context = {
            'form_osoba':form_osoba,
            'form_grupa':form_grupa,
        }
        return render(request, 'dodaj_osobe.html', context)

    def post(self, request):
        form_osoba = FormOsoba(request.POST)
        form_grupa = FormGrupy(request.POST)

        if form_osoba.is_valid() and form_grupa.is_valid():

            osoba=Osoba.objects.create(**form_osoba.cleaned_data)

            form_osoba.save(commit=True)
            form_grupa.save(commit=True)

            return redirect('userstories:osoba_info', id=osoba.id)

        else:
            print("Formularz niepoprawnie wypełniony")

        context = {
            'form_osoba': form_osoba,
            'form_grupa': form_grupa,
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

        dana_osoba = Osoba.objects.get(id=id)

        form_osoba = FormOsoba(request.POST)
        form_adres = FormAdres(request.POST)
        form_telefon = FormTelefon(request.POST)
        form_email = FormEmail(request.POST)

        if (form_osoba.is_valid and form_adres.is_valid and form_telefon.is_valid and form_email.is_valid):

            form_osoba.save(commit=True)
            form_adres.save(commit=True)
            form_telefon.save(commit=True)
            form_email.save(commit=True)

            return redirect('userstories:osoba_info', dana_osoba)

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
    def get(self, request, id):
        osoba = Osoba.objects.get(id=id)
        form_osoba = FormOsoba(instance=osoba)
        context = {
            'form_osoba': form_osoba
        }

        return render(request, "usun_osobe.html", context)

    def post(self, request, id):
        osoba = Osoba.objects.get(id=id)
        osoba.delete()

        return redirect('index')

#Część dotycząca grup

class ListaGrup(View):
    """ Ma za zadanie pokazać wszystkie dostepne grupy"""
    def get(self, request):
        lista_grup = Grupy.objects.all()
        context = {
            'lista_grup':lista_grup
        }
        return render(request, "lista_grup.html", context)

class DodajGrupe(View):
    """Dodaje nową grupę"""
    def get(self, request):

        form_grupa = FormGrupy()

        context = {'form_grupa':form_grupa}

        return render(request, "dodaj_grupe.html", context)

    def post(self, request):

        form_grupa = FormGrupy(request.POST)

        if form_grupa.is_valid():

            form_grupa.save(commit=True)

            return redirect('userstories:lista_grup')

        context ={'form_grupa':form_grupa}

        return render(request, "dodaj_grupe.html", context)

class GrupaInfo(View):
    """Wyświetla informacje szczegółowe o danej grupie"""
    def get(self, request, id):
        grupy = Grupy.objects.get(pk=id)
        osoby = grupy.osoby.all()
        context = {
            'grupy':grupy,
            'uczestnicy':osoby,
        }
        return render(request, "grupa_info.html", context)

class EdytujGrupe(View):
    """Modyfikacja grupy"""
    def get(self, request, id):
        grupy = Grupy.objects.get(pk=id)
        form_grupa = FormGrupy(instance=grupy)
        context = {'form_grupa': form_grupa}
        return render(request, "edytuj_grupe.html", context)

    def post(self, request, id):
        grupy = Grupy.objects.get(pk=id)
        form_grupa = FormGrupy(request.POST,instance=grupy)
        if form_grupa.is_valid():
            grupy = form_grupa.save()
            return redirect('userstories:grupy_info', id=grupy.id)
        context = {
            'form_grupa':form_grupa
        }
        return render(request, "edytuj_grupe.html", context)

class UsunGrupe(View):
    """Usuwanie wcześniej utworzonej grupy"""
    def get(self, request, id):
        grupy = Grupy.objects.get(pk=id)
        form_grupa = FormGrupy(instance=grupy)
        context = {
            'form_grupa': form_grupa
        }

        return render(request, "usun_grupe.html", context)
    def post(self, request, id):
        grupy = Grupy.objects.get(pk=id)
        grupy.delete()
        return redirect('userstories:lista_grup')













class Szukaj(View):

    def get(self, request):

        return render(request, "szukaj.html")

    def post(self, request):

        if request.POST.get('firstname'):
            osoba = Osoba.objects.filter(firstname__contains = request.POST['firstname'])
            return render_to_response('szukaj.html', {'lista_osob': osoba})

        if request.POST.get('surname'):
            osoba = Osoba.objects.filter(surname__contains = request.POST['surname'])
            return render_to_response('szukaj.html', {'lista_osob': osoba})



def relative(request):
    return render(request, "relative_url_templates.html")

