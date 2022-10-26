from django.contrib import admin
from ..models import Store

class StoreAdmin(admin.ModelAdmin):
    list_display = ('brandName', 'document', 'email', 'state', 'status', 'paymentStatus')
    list_filter = ('state', 'status', 'paymentStatus')

admin.site.register(Store, StoreAdmin)