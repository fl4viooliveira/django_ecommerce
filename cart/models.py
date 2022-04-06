from decimal import Decimal
from typing import Tuple

from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name: str = 'Category'
        verbose_name_plural: str = "Categories"

    def __str__(self) -> str:
        return self.name


class Address(models.Model):
    SHIPPING_ADDRESS_TYPE: str = 'S'
    BILLING_ADDRESS_TYPE: str = 'B'
    ADDRESS_CHOICES: Tuple[Tuple[str, str], ...] = (
        (BILLING_ADDRESS_TYPE, 'Billing'),
        (SHIPPING_ADDRESS_TYPE, 'Shipping'),
    )

    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    default = models.BooleanField(default=False)
    address_line_1 = models.CharField(max_length=150)
    address_line_2 = models.CharField(max_length=150)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)

    class Meta:
        verbose_name: str = 'Address'
        verbose_name_plural: str = 'Addresses'

    def __str__(self) -> str:
        return ', '.join([
            self.address_line_1,
            self.address_line_2,
            self.city,
            self.zip_code,
        ])


class ColourVariation(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class SizeVariation(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    description = models.TextField()
    slug = models.SlugField(unique=True)
    stock = models.IntegerField(default=0)
    title = models.CharField(max_length=150)
    active = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='product_images')
    available_sizes = models.ManyToManyField(SizeVariation)
    available_colours = models.ManyToManyField(ColourVariation)
    secondary_categories = models.ManyToManyField(to=Category, blank=True)
    price = models.DecimalField(default=0, max_digits=9, decimal_places=2, )
    primary_category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        related_name='primary_products',
        blank=True, null=True,
    )

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(value=self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self) -> str:
        return reverse("cart:product-detail", kwargs={'slug': self.slug})

    def get_update_url(self) -> str:
        return reverse("staff:product-update", kwargs={'pk': self.pk})

    def get_delete_url(self) -> str:
        return reverse("staff:product-delete", kwargs={'pk': self.pk})

    def get_price(self) -> str:
        return "{:.2f}".format(self.price / 100)

    @property
    def in_stock(self) -> bool:
        return self.stock > 0


class OrderItem(models.Model):
    quantity = models.PositiveIntegerField(default=1)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    size = models.ForeignKey(to=SizeVariation, on_delete=models.CASCADE)
    colour = models.ForeignKey(to=ColourVariation, on_delete=models.CASCADE)
    order = models.ForeignKey(
        to="Order",
        related_name='items',
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f"{self.quantity} x {self.product.title}"

    def get_raw_total_item_price(self) -> Decimal:
        return self.quantity * self.product.price

    def get_total_item_price(self) -> str:
        price = self.get_raw_total_item_price()  # 1000
        return "{:.2f}".format(price / 100)


class Order(models.Model):
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(blank=True, null=True)
    ordered = models.BooleanField(default=False)
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        blank=True, null=True,
    )
    billing_address = models.ForeignKey(
        to=Address,
        on_delete=models.SET_NULL,
        related_name='billing_address',
        blank=True, null=True,
    )
    shipping_address = models.ForeignKey(
        to=Address,
        on_delete=models.SET_NULL,
        related_name='shipping_address',
        blank=True, null=True,
    )

    def __str__(self) -> str:
        return self.reference_number

    @property
    def reference_number(self) -> str:
        return f"ORDER-{self.pk}"

    def get_raw_subtotal(self) -> float:
        total = 0
        for order_item in self.items.all():
            total += order_item.get_raw_total_item_price()
        return total

    def get_subtotal(self) -> str:
        subtotal = self.get_raw_subtotal()
        return "{:.2f}".format(subtotal / 100)

    def get_raw_total(self) -> float:
        subtotal = self.get_raw_subtotal()
        # add tax, add delivery, subtract discounts
        # total = subtotal - discounts + tax + delivery
        return subtotal

    def get_total(self) -> str:
        total = self.get_raw_total()
        return "{:.2f}".format(total / 100)


class Payment(models.Model):
    PAYPAL_PAYMENT_METHOD: str = 'PayPal'

    PAYMENT_METHODS: Tuple[Tuple[str, str], ...] = (
        (PAYPAL_PAYMENT_METHOD, 'PayPal'),
    )

    amount = models.FloatField()
    raw_response = models.TextField()
    successful = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS, )
    order = models.ForeignKey(
        to=Order,
        on_delete=models.CASCADE,
        related_name='payments',
    )

    def __str__(self) -> str:
        return self.reference_number

    @property
    def reference_number(self):
        return f"PAYMENT-{self.order}-{self.pk}"


class StripePayment(models.Model):
    amount = models.FloatField(default=0)
    successful = models.BooleanField(default=False)
    payment_intent_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(
        to=Order,
        on_delete=models.CASCADE,
        related_name='stripe_payments',
    )

    def __str__(self) -> str:
        return self.reference_number

    @property
    def reference_number(self) -> str:
        return f"STRIPE-PAYMENT-{self.order}-{self.pk}"


__all__ = (
    'Category',
    'Address',
    'ColourVariation',
    'SizeVariation',
    'Product',
    'OrderItem',
    'Order',
    'Payment',
    'StripePayment',
)
