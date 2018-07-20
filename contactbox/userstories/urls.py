from django.conf.urls import url
from userstories import views
from .views import *

# To jest specjalnie żeby użyć TEMPLATE TAGGING
app_name = 'userstories'

urlpatterns=[
    url(r'^mapa_aplikacji/$',Relative.as_view(), name='mapa_aplikacji'),
    url(r'^dodaj_osobe/$',DodajOsobe.as_view(), name="dodaj_osobe"),
    url(r'^modify/(?P<id>[0-9]+)/$',EdytujOsobe.as_view(), name="edytuj_osobe"),
    url(r'^show/(?P<id>[0-9]+)/$',OsobaInfo.as_view(), name="osoba_info"),
    url(r'^delete/(?P<id>[0-9]+)/$',UsunOsobe.as_view(), name="usun_osobe"),
    url(r'^dodaj_grupe/$',DodajGrupe.as_view(), name="dodaj_grupe"),
    url(r'^edytuj_grupe/(?P<id>[0-9]+)/$',EdytujGrupe.as_view(), name="edytuj_grupe"),
    url(r'^grupa_info/(?P<id>[0-9]+)/$',GrupaInfo.as_view(), name="grupa_info"),
    url(r'^usun_grupe/(?P<id>[0-9]+)/$',UsunGrupe.as_view(), name="usun_grupe"),
    url(r'^lista_grup/$',ListaGrup.as_view(), name="lista_grup"),
    url(r'^szukaj/$',Szukaj.as_view(), name="szukaj"),
]