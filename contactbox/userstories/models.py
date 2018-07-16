from django.db import models

# Create your models here.

class Adres(models.Model):
    city = models.CharField(max_length=64, verbose_name='Miasto', blank=True, null=True)
    street_name = models.CharField(max_length=64, verbose_name='Ulica', blank=True, null=True)
    street_number = models.CharField(max_length=64, verbose_name='Numer domu', blank=True, null=True)
    flat_number = models.CharField(max_length=64, verbose_name='Numer mieszkania', blank=True, null=True)

    def __str__(self):
        return "{} {} {} {}".format(self.city, self.street_name, self.street_number, self.flat_number)


class Osoba(models.Model):
    firstname = models.CharField(max_length=64, verbose_name='Imię')
    surname = models.CharField(max_length=64, verbose_name='Nazwisko')
    description = models.CharField(max_length=128, verbose_name='Opis', null=True)
    adres = models.ForeignKey(Adres, related_name='osoba', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "{} {}".format(self.firstname, self.surname)

PHONE_CHOICES = (
    (1, "telefon domowy"),
    (2, "telefon służbowy"),
    (3, "telefon komórkowy"),
)

class Telefon(models.Model):
    phone_number = models.CharField(max_length=12,verbose_name='Numer telefonu', blank=True, null=True)
    phone_type = models.IntegerField(choices=PHONE_CHOICES, verbose_name='Rodzaj telefonu', null=True)
    osoba = models.ForeignKey(Osoba, related_name='telefon', on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.phone_number, self.phone_type)

EMAIL_CHOICES = (
    (1, "email prywatny"),
    (2, "email służbowy"),

)

class Email(models.Model):
    email_address = models.EmailField(blank=True, verbose_name='Adres emailowy', null=True)
    email_type = models.IntegerField(choices=EMAIL_CHOICES, verbose_name='rodzaj adresu', null=True)
    osoba = models.ForeignKey(Osoba, related_name='email', on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.email_address, self.email_type)


class Grupy(models.Model):
    group_name = models.CharField(max_length=64, default='podstawowa')
    osoby = models.ManyToManyField(Osoba, related_name='grupy')

    def __str__(self):
        return self.group_name

