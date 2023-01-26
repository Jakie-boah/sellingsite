from users.models import UserProfile
from django.core.management.base import BaseCommand
from loguru import logger


class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not UserProfile.objects.filter(username='Admin').exists():
            UserProfile.objects.create_superuser(
                username='Admin',
                password='qwerty100',
                login='Admin'
            )
            logger.info('Админ добавлен')
        else:
            logger.info('Этот админ уже есть')
