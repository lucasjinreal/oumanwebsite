from django.db import models


# Create your models here.
class BusinessContact(models.Model):
    contact_time = models.DateTimeField(auto_now_add=True)
    contact_company = models.CharField(max_length=50, blank=True)
    contact_email = models.EmailField(max_length=30, blank=True)
    contact_name = models.CharField(max_length=20, blank=True)
    contact_occupation = models.CharField(max_length=20, blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    contact_detail = models.TextField(max_length=50, blank=True)

    def __str__(self):
        return self.contact_company




