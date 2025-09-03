from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    password = models.CharField()
    
    def __str__(self):
        return self.name
    