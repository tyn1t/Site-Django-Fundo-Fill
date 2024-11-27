from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Fill(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=8, null=False, blank=False)
    valor = models.FloatField(null=False, blank=False)
    cota_qtd = models.IntegerField(null=False, blank=False)
    dividendos = models.FloatField(null=True, blank=True)
    dividendo_total = models.FloatField(null=True, blank=True)

    
    def __str__(self) -> str:
        return self.name.upper()
    
    class Meta:
        ordering = ['id', 'name']
    

    
   
