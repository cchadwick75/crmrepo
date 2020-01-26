from django.db import models
from django.contrib.auth.models import User
from administration.models import Customer

# Create your models here.
class CustomerGetStatus(models.Model):
    class Meta:
        permissions = (("access_customer_form", "Can access the form"),)






