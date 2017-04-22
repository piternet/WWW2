from django.db import models

class Kandydat(models.Model):
    nazwa = models.CharField(max_length=200)
    def __str__(self):
        return self.nazwa

class Wojewodztwo(models.Model):
    nazwa = models.CharField(max_length=200)
    def __str__(self):
        return self.nazwa

class Okreg(models.Model):
    numer = models.IntegerField()
    wojewodztwo = models.ForeignKey(Wojewodztwo)
    def __str__(self):
        return ', '.join([str(self.numer), self.wojewodztwo])

class Gmina(models.Model):
    nazwa = models.CharField(max_length=200)
    kod = models.CharField(max_length=10)
    powiat = models.CharField(max_length=200)
    okreg = models.ForeignKey(Okreg, default='')
    def __str__(self):
        return self.kod + ": " + ', '.join([self.nazwa, self.powiat, self.okreg])

class Obwod(models.Model):
    numer = models.IntegerField()
    gmina = models.ForeignKey(Gmina)
    okreg = models.ForeignKey(Okreg)
    nazwa = models.CharField(max_length=200)
    uprawnieni = models.IntegerField(default=0)
    kartyWydane = models.IntegerField(default=0)
    glosyOddane = models.IntegerField(default=0)
    glosyNiewazne = models.IntegerField(default=0)
    glosyWazne = models.IntegerField(default=0)
    def str_frekwencja(self):
        return ', '.join([str(uprawnieni), str(kartyWydane), str(glosyOddane), str(glosyNiewazne), str(glosyWazne)])
    def __str__(self):
        return ', '.join([str(numer), gmina, okreg, nazwa, self.str_frekwencja()])

class Wynik(models.Model):
    kandydat = models.ForeignKey(Kandydat)
    obwod = models.ForeignKey(Obwod)
    wynik = models.IntegerField(default=0)
    def __str__(self):
        return ', '.join([self.kandydatId, self.obwodId, str(self.wynik)])
