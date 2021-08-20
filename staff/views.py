from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.views import generic

from cart.models import (Order, Product)
from .forms import ProductForm
from .mixins import StaffUserMixin


class StaffView(LoginRequiredMixin, StaffUserMixin, generic.ListView):
    template_name = 'staff/staff.html'
    queryset = Order.objects.filter(ordered=True).order_by('-ordered_date')
    paginate_by: int = 20
    context_object_name: str = 'orders'


class ProductListView(LoginRequiredMixin, StaffUserMixin, generic.ListView):
    template_name: str = 'staff/product_list.html'
    queryset = Product.objects.all()
    paginate_by: int = 20
    context_object_name: str = 'products'


class ProductCreateView(LoginRequiredMixin, StaffUserMixin, generic.CreateView):
    template_name: str = 'staff/product_create.html'
    form_class = ProductForm

    def get_success_url(self) -> str:
        return reverse('staff:product-list')

    def form_valid(self, form) -> HttpResponseRedirect:
        form.save()
        return super(ProductCreateView, self).form_valid(form)


class ProductUpdateView(LoginRequiredMixin, StaffUserMixin, generic.UpdateView):
    template_name: str = 'staff/product_create.html'
    form_class = ProductForm
    queryset = Product.objects.all()

    def get_success_url(self) -> str:
        return reverse("staff:product-list")

    def form_valid(self, form) -> HttpResponseRedirect:
        form.save()
        return super(ProductUpdateView, self).form_valid(form)


class ProductDeleteView(LoginRequiredMixin, StaffUserMixin, generic.DeleteView):
    template_name: str = 'staff/product_delete.html'
    queryset = Product.objects.all()

    def get_success_url(self) -> str:
        return reverse("staff:product-list")


__all__ = (
    'StaffView',
    'ProductListView',
    'ProductCreateView',
    'ProductUpdateView',
    'ProductDeleteView',
)
