from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .models import Trek, Store


@receiver(post_save, sender=Trek)
def save_trek(sender, instance: Trek, created, **kwargs):

    user = instance.owner

    if instance.store_user != user.store:
        instance.store_user = user.store
        instance.save()


@receiver(post_save, sender=Trek)
def is_archived_trek(sender, instance: Trek, created, **kwargs):

    if instance.store:

        if instance.client:

            if instance.store_user and not (instance.is_archived):

                instance.is_archived = True
                instance.save()
