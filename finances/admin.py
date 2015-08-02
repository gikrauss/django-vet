from django.contrib import admin
from finances.models import Item, Sales, Provider

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'cat', 'price', 'stock')

class SalesAdmin(admin.ModelAdmin):
	list_display = ('date', 'item', 'client')

class ProviderAdmin(admin.ModelAdmin):
	list_display = ('name', 'phone', 'email')


admin.site.register(Item, ItemAdmin)
admin.site.register(Sales, SalesAdmin)
admin.site.register(Provider, ProviderAdmin)