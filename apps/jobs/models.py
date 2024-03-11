
# Create your models here.
from django.db import models

# create a job model
class Jobs(models.Model):
    id= models.IntegerField(primary_key=True)
    name=models.CharField(max_length=200)