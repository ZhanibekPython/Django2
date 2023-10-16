from django.apps import apps
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Returns all articles'

    def handle(self, *args, **options):
        Model1 = apps.get_model('Sem1', 'Article')
        articles = Model1.objects.all()
        self.stdout.write(f'{articles}')
