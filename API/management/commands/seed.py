from django.core.management.base import BaseCommand
from API.factories import CategoryFactory, OfferFactory


class Command(BaseCommand):
    help = 'Generate fake data and seed the models with them, default are 10'

    def add_arguments(self, parser):
        parser.add_argument('--amount', type=int,
                            help="The amount of fake data you want")

    def _generate_data(self, amount: int):
        for _ in range(amount):
            CategoryFactory()
            OfferFactory()

    def handle(self, *args, **options):
        amount = options.get('amount') or 10
        self._generate_data(amount)
