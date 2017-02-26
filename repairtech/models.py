from django.db import models


# Create your models here.
class RepairOrder(models.Model):
    order_time = models.DateTimeField(auto_now_add=True)
    order_repair_time_start = models.DateTimeField(max_length=20, blank=True)
    order_repair_time_end = models.DateTimeField(max_length=20, blank=True)
    order_contact_name = models.CharField(max_length=20, blank=True)
    order_contact_id = models.CharField(max_length=20, blank=True)
    order_contact_qq = models.CharField(max_length=30, blank=True)
    order_contact_phone = models.CharField(max_length=20, blank=False)
    order_contact_address = models.CharField(max_length=50, blank=True)
    order_detail = models.TextField(blank=True)

    def __str__(self):
        return self.order_contact_name
