from django.db.models.signals import post_delete
from django.dispatch import receiver

from .models import BlackList
from items_window.models import Item


@receiver(post_delete, sender=BlackList)
def unban_objects(sender, instance, using, **kwargs):
    all_items = Item.objects.filter(phone_number=instance.phone_number).all()
    for i in all_items:
        i.banned = False
        i.save()

