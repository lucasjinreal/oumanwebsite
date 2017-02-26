from django.contrib import admin
from repairtech.models import RepairOrder


class RepairOrderAdmin(admin.ModelAdmin):
    list_display = ('order_time', 'order_repair_time_start', 'order_repair_time_end', 'order_contact_name',
                    'order_contact_phone', 'order_contact_address')
# Register your models here.
admin.site.register(RepairOrder, RepairOrderAdmin)