from django.db import models

# Create your models here.
class nature(models.Model):
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=100)   #  create a model 
    number=models.IntegerField(10)
    def __str__(self):
        return self.name
       
