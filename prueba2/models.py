from django.db import models
# Create your models here.
  
class genNum(models.Model):
   x1 = models.FloatField(blank=True, null=True)
   x2 = models.FloatField(blank=True, null=True)
   x3 = models.FloatField(blank=True, null=True)    

def __str__(self):
   return str(self.x1) + " , " + str(self.x2) + " , " + str(self.x3)
