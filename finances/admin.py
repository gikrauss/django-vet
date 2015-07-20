from django.contrib import admin
from finances.models import Item, Sales

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'cat', 'price', 'stock')

class SalesAdmin(admin.ModelAdmin):
	list_display = ('date', 'item', 'client')


admin.site.register(Item, ItemAdmin)
admin.site.register(Sales, SalesAdmin)