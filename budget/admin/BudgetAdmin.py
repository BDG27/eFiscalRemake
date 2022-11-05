from django.contrib import admin
from ..models import Budget
from admin_auto_filters.filters import AutocompleteFilter, AutocompleteFilterFactory
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter

class BudgetAdmin(admin.ModelAdmin):
    list_display = ('store', 'number', 'emissionDate','amount', 'status')
    list_display_links = ('store', 'number', 'emissionDate')
    list_filter = [
        ('store', RelatedDropdownFilter),
        ('status', ChoiceDropdownFilter),
    ]
    search_fields = ['store_brandName', 'number', 'emissionDate']

admin.site.register(Budget, BudgetAdmin)