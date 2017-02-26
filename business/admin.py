from django.contrib import admin
from business.models import BusinessContact


# Register your models here.
class BusinessContactAdmin(admin.ModelAdmin):
    list_display = ('contact_time', 'contact_company', 'contact_email', 'contact_name', 'contact_occupation',)

admin.site.register(BusinessContact, BusinessContactAdmin)
