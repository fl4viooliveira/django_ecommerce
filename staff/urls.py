from typing import List

from django.urls import (path, URLPattern)

from . import views

urlpatterns: List[URLPattern] = [
    path(route='', view=views.StaffView.as_view(), name='staff'),
    path(route='products/', view=views.ProductListView.as_view(), name='product-list'),
    path(route='create/', view=views.ProductCreateView.as_view(), name='product-create'),
    path(
        route='products/<pk>/update/',
        view=views.ProductUpdateView.as_view(),
        name='product-update',
    ),
    path(
        route='products/<pk>/delete/',
        view=views.ProductDeleteView.as_view(),
        name='product-delete',
    ),
]

app_name: str = 'staff'

__all__ = ('app_name', 'urlpatterns',)
