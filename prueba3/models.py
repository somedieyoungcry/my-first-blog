from django.db import models
from django.db.models import Model
# Create your models here.
  
class genNum2(models.Model):
    net = models.IntegerField(blank=True, null=True)
    net2 = models.IntegerField(blank=True, null=True)
    net3 = models.IntegerField(blank=True, null=True)
    net4 = models.IntegerField(blank=True, null=True)
    net5 = models.IntegerField(blank=True, null=True)
    flop = models.FloatField(blank=True, null=True)
    
    def __str__(self):
        return str(self.net)
    