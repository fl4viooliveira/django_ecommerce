from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Customer

User = get_user_model()


@receiver(signal=post_save, sender=User)
def post_save_user_receiver(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)


__all__ = ('post_save_user_receiver',)
