from django.core.management import BaseCommand

from exam.utils import fill_db


class Command(BaseCommand):
    help = 'The Zen of Python'

    def handle(self, *args, **options):
        fill_db()
