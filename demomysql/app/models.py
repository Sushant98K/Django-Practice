from django.db import models

# Create your models here.
class Demodata(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=100)
    
    
    
    #shows object titel in admin panel 
    def __str__(self):
        return self.name