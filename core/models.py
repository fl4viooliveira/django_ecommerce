from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save

User = get_user_model()


class Customer(models.Model):
    stripe_customer_id = models.CharField(max_length=100)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.email


def post_save_user_receiver(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)


post_save.connect(post_save_user_receiver, sender=User)
