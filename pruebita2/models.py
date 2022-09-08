from django.db import models

# Create your models here.
class post3(models.Model):
   p1 = models.FloatField(blank=True, null=True)
   p2 = models.FloatField(blank=True, null=True)
   p3 = models.FloatField(blank=True, null=True)    
   
def __str__(self):
   return str(self.p1) + ' , ' + str(self.p2) + ' , ' + str(self.p3)
