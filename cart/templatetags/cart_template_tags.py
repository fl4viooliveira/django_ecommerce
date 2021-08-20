from django import template

from cart.utils import get_or_set_order_session

register = template.Library()


@register.filter
def cart_item_count(request) -> int:
    order = get_or_set_order_session(request)
    count: int = order.items.count()
    return count


__all__ = ('cart_item_count',)
