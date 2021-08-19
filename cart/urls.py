from typing import List

from django.urls import (path, URLPattern)

from . import views

urlpatterns: List[URLPattern] = [
    path(route='', view=views.CartView.as_view(), name='summary'),
    path(route='payment/', view=views.PaymentView.as_view(), name='payment'),
    path(route='checkout/', view=views.CheckoutView.as_view(), name='checkout'),
    path(route='thank-you/', view=views.ThankYouView.as_view(), name='thank-you'),
    path(route='shop/', view=views.ProductListView.as_view(), name='product-list'),
    path(route='orders/<pk>/', view=views.OrderDetailView.as_view(), name='order-detail'),
    path(route='webhooks/stripe/', view=views.stripe_webhook_view, name='stripe-webhook'),
    path(route='shop/<slug>/', view=views.ProductDetailView.as_view(), name='product-detail'),
    path(route='confirm-order/', view=views.ConfirmOrderView.as_view(), name='confirm-order'),
    path(route='payment/stripe/', view=views.StripePaymentView.as_view(), name='payment-stripe'),
    path(
        route='increase-quantity/<pk>/',
        view=views.IncreaseQuantityView.as_view(),
        name='increase-quantity',
    ),
    path(
        route='decrease-quantity/<pk>/',
        view=views.DecreaseQuantityView.as_view(),
        name='decrease-quantity',
    ),
    path(
        route='remove-from-cart/<pk>/',
        view=views.RemoveFromCartView.as_view(),
        name='remove-from-cart',
    ),
]

app_name: str = 'cart'

__all__ = ('app_name', 'urlpatterns',)
