from django.contrib import admin
from .models import Order, OrderLineItem, PromoCode


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'user_profile', 'date',
                       'delivery_cost', 'order_total',
                       'total', 'original_cart',
                       'stripe_pid')

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'total', 'original_cart',
              'stripe_pid')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'total',)

    ordering = ('-date',)


class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'user']


admin.site.register(Order, OrderAdmin)
admin.site.register(PromoCode, PromoCodeAdmin)
