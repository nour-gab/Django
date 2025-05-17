from django.contrib import admin, messages
from django.db.models.aggregates import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse
from django.contrib.contenttypes.admin import GenericTabularInline
from tags.models import TggedItem
from . import models

# Register your models here.

#admin.site.register(models.Product, ProductAdmin)
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['collection']
    # prepopulated_fields = {
    #     'slug':['title']
    # }
    actions = ['clear_inventory']
    list_display = ['title', 'price', 'inventory_status', 'collection']
    list_editable = ['price']
    list_per_page = 10

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'low'
        return 'ok'
    
    @admin.action(description='Clear Inventory')
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory= 0)
        self.message_user(
            request,
            f'{updated_count} products were sucecessfully updated.',
            messages.SUCCESS
        )

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    list_per_page = 10
    ordering = ['last_name', 'first_name']
    search_fields = ['last_name__istartswith', 'first_name__istartswith']

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'product_count']
    
    @admin.display(ordering= 'product_count')
    def product_count(self, collection):
        #reverse(admin:app_model_page)
        url = (reverse('admin:store_product_changelist') 
               + '?'
               + urlencode({
                   'collection__id': str(collection.id)
               }))
        return format_html('<a href="{}"> {} </a>', url, collection.product_count)

    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            product_count = Count('product')
        )


class OrderItemInline(admin.TabularInline):
    model= models.OrderItem
    extra = 0
    min_num=1

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at', 'customer']
    inlines=[OrderItemInline]
    fields = ['customer', 'payement_status'] 