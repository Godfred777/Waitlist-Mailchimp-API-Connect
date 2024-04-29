from django.db import models

# Create your models here.
class WaitlistContact(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField(unique=True)
    subscription_status = models.CharField(max_length=2, default='pending')