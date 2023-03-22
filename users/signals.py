from django.dispatch import receiver
from django.db.models.signals import pre_save
from loguru import logger
from django.contrib.auth import get_user_model

UserModel = get_user_model()


@receiver(pre_save, sender=UserModel)
def set_new_user_inactive(sender, instance, **kwargs):
    if instance._state.adding is True:
        logger.info("Creating Inactive User")
        instance.is_active = False

