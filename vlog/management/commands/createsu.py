from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os

class Command(BaseCommand):
    help = 'Creates a superuser'

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                password=os.environ.get('DJANGO_ADMIN_PASSWORD', 'defaultpassword'),
                email='admin@example.com'
            )
            self.stdout.write(self.style.SUCCESS('Superuser has been created'))
