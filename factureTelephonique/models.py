from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.

# la creation de la classe client

class Client(models.Model):
    nomClient = models.CharField(max_length=200, verbose_name="Nom du client")
    numClient = models.CharField(max_length=200, verbose_name="Télephone")

    def __str__(self):
        return "%s %s" % (self.nomClient, self.numClient)


# la creation de la classe facture
class Facture(models.Model):
    dureeTotal = models.CharField(max_length=20, verbose_name="Durée total")
    montant = models.DecimalField(validators=[MinValueValidator(0)], decimal_places=2, max_digits=12)
    # montant=models.FloatField()
    client = models.ForeignKey('Client', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "%s %s" % (self.dureeTotal, self.montant)


# crete la classe CDR
class Cdr(models.Model):
    # date = models.DateField(auto_now_add= True)# ne s affiche pas dans la partie forms !!!!
    date = models.DateTimeField()
    dureeAppel = models.CharField(max_length=20 ,verbose_name="durée de l'appel")
    # client = models.ForeignKey('Client', on_delete=models.CASCADE,null=True)
    facture = models.ForeignKey('Facture', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date)
    class Meta:
        ordering= ["-date"]
