from typing import List

from django.contrib import admin

from .models import (
    Product,
    OrderItem,
    Order,
    ColourVariation,
    SizeVariation,
    Address,
    Payment,
    Category,
    StripePayment,
)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display: List[str] = [
        'address_line_1',
        'address_line_2',
        'city',
        'zip_code',
        'address_type',
    ]


admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Payment)
admin.site.register(Category)
admin.site.register(OrderItem)
admin.site.register(SizeVariation)
admin.site.register(StripePayment)
admin.site.register(ColourVariation)
