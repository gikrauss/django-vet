from django.contrib import admin
from finances.models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'cat', 'price', 'stock')


admin.site.register(Item, ItemAdmin)