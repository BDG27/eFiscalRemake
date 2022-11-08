from django.contrib import admin
from ..models import Budget, Product
from admin_auto_filters.filters import AutocompleteFilter, AutocompleteFilterFactory
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter

class ProductAdmin(admin.ModelAdmin):
    list_display = ('budget', 'description', 'unityValue','quantity')
    list_display_links = ('budget', 'description', 'unityValue')
    list_filter = [
        ('budget', RelatedDropdownFilter),
        ('budget__store', RelatedDropdownFilter),
    ]
    search_fields = ['budget__number', 'description', 'budget__store__corporateName']

admin.site.register(Product, ProductAdmin)