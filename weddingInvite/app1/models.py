from django.db import models

# Create your models here.


class ConfirmationOfPresence(models.Model):
    prenume = models.CharField(max_length=100)
    nume = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    număr_telefon = models.CharField(max_length=30)
    număr_adulți = models.IntegerField()
    număr_copii = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.prenume} -> {self.nume}'


class PersonalizedInvitation(models.Model):
    nume_mireasă = models.CharField(max_length=100)
    nume_mire = models.CharField(max_length=100)
    dată_eveniment = models.CharField(max_length=100)
    părinții_miresei = models.CharField(max_length=100)
    părinții_mirelui = models.CharField(max_length=100)
    nume_nașă = models.CharField(max_length=100)
    nume_naș = models.CharField(max_length=100)
    nume_biserică = models.CharField(max_length=100)
    ora_cununie_religioasă = models.CharField(max_length=100)
    local_petrecere = models.CharField(max_length=100)
    ora_petrecere = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nume_mireasă} -> {self.nume_mire}'

