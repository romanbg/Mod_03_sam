# Generated by Django 2.0.5 on 2018-07-16 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userstories', '0005_auto_20180714_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adres',
            name='flat_number',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Numer mieszkania'),
        ),
        migrations.AlterField(
            model_name='email',
            name='email_address',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Adres emailowy'),
        ),
        migrations.AlterField(
            model_name='email',
            name='email_type',
            field=models.IntegerField(choices=[(1, 'email prywatny'), (2, 'email służbowy')], null=True, verbose_name='rodzaj adresu'),
        ),
        migrations.AlterField(
            model_name='osoba',
            name='description',
            field=models.CharField(max_length=128, null=True, verbose_name='Opis'),
        ),
        migrations.AlterField(
            model_name='osoba',
            name='firstname',
            field=models.CharField(max_length=64, verbose_name='Imię'),
        ),
        migrations.AlterField(
            model_name='osoba',
            name='surname',
            field=models.CharField(max_length=64, verbose_name='Nazwisko'),
        ),
        migrations.AlterField(
            model_name='telefon',
            name='phone_number',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Numer telefonu'),
        ),
        migrations.AlterField(
            model_name='telefon',
            name='phone_type',
            field=models.IntegerField(choices=[(1, 'telefon domowy'), (2, 'telefon służbowy'), (3, 'telefon komórkowy')], null=True, verbose_name='Rodzaj telefonu'),
        ),
    ]