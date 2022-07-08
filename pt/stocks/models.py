from datetime import datetime
from operator import mod
from django.db import models

# Create your models here.



class Fabrics(models.Model):
    partycode = models.CharField(max_length=10,)
    color = models.PositiveIntegerField()
    meter = models.DecimalField(max_digits=6, decimal_places=3)
    fabric = models.CharField(max_length=20)
    maker = models.CharField(max_length=15)
    time = models.DateTimeField(default=datetime.now())
    cutting = models.PositiveIntegerField(default=0)
    item = models.CharField(max_length=20,blank=True)
    cut_time = models.DateTimeField(null=True)
    rec_pcs = models.PositiveIntegerField(default=0)
    gr_pcs = models.PositiveIntegerField(default=0)
    completed = models.BooleanField(default=False)
    hsb_clr = models.BooleanField(default=False)


class Makers(models.Model):
    maker = models.CharField(max_length=20)
    def __str__(self):
         return self.maker

class Items(models.Model):
    maker = models.ManyToManyField(Makers)
    item = models.CharField(max_length=20)
    rate = models.DecimalField(max_digits=6,decimal_places=2)
    def get_maker(self):
        return ','.join([p.maker for p in self.maker.all()])

class Partycodes(models.Model):
    partycode = models.CharField(max_length=20)

class Fabnames(models.Model):
    fabname = models.CharField(max_length=20)