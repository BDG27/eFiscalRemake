from django.contrib import admin
from ..models import Client
from admin_auto_filters.filters import AutocompleteFilter, AutocompleteFilterFactory
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter

class ClientAdmin(admin.ModelAdmin):
    list_display = ('corporateName', 'document', 'store','state', 'status')
    list_display_links = ('corporateName', 'document', 'store')
    list_filter = [
        ('state', ChoiceDropdownFilter),
        ('status', ChoiceDropdownFilter),
    ]
    search_fields = ['corporateName', 'document', 'store__brandName', 'state']

admin.site.register(Client, ClientAdmin)