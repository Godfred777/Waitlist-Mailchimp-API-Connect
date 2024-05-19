from django.db import models

# Create your models here.
class WaitlistContact(models.Model):
    email = models.EmailField(unique=True)
    subscription_status = models.CharField(max_length=2, default='pending')