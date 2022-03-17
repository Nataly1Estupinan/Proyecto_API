from django.db import models

# Create your models here.
class Persona(models.Model):
    TDocument_Type=models.CharField(max_length=100)
    document=models.PositiveIntegerField()
    names=models.CharField(max_length=200)
    last_names=models.CharField(max_length=200)
    hobbie=models.CharField(max_length=100)

