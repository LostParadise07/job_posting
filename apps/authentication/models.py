
# Create your models here.
from django.db import models

# UserDetails
class UserDetails(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=20)
    user_email = models.EmailField(max_length=20)
    user_password = models.CharField(max_length=20)
    user_mobile = models.CharField(max_length=13)
    user_address = models.CharField(max_length=100)
    user_role = models.Choices('Admin', 'User')