from django.contrib import admin
from ..models import Store
from admin_auto_filters.filters import AutocompleteFilter, AutocompleteFilterFactory
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter

class StoreAdmin(admin.ModelAdmin):
    list_display = ('brandName', 'document', 'email', 'state', 'status', 'paymentStatus')
    list_display_links = ('brandName', 'document', 'email')
    search_fields = ['brandName', 'document', 'email', 'state']
    list_filter = [
        # AutocompleteFilterFactory('Estado', 'state', '', True), 
        ('state', ChoiceDropdownFilter),
        ('status', ChoiceDropdownFilter),
        ('paymentStatus', ChoiceDropdownFilter),
    ]

admin.site.register(Store, StoreAdmin)