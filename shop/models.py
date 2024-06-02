from django.db import models

# Create your models here.
class Contractmodel(models.Model):
    full_name=models.CharField(max_length=200)
    email=models.EmailField(max_length=30)
    subject=models.CharField(max_length=100)
    description=models.TextField(max_length=250)

    def __str__(self):
         return self.id
    


     
