from random import randint

import factory
from factory.django import DjangoModelFactory
from factory.faker import Faker
from factory import Sequence, PostGenerationMethodCall, sequence, RelatedFactory, RelatedFactoryList
from factory import SubFactory

from API.models import Category


class CategoryFactory(DjangoModelFactory):
    id = None
    name = None

    @sequence
    def name(n):
        try:
            max_id = Category.objects.latest('id').id
            return f'Category-{max_id + 1}'
        except Category.DoesNotExist:
            return f'Category-0'

    @sequence
    def id(n):
        try:
            current_id = Category.objects.latest('id').id
            return current_id + 1
        except Category.DoesNotExist:
            return 1

    class Meta:
        model = 'API.Category'


class OfferFactory(DjangoModelFactory):
    title = Faker('word')
    description = Faker('paragraph')
    price = Faker('credit_card_security_code')
    category = factory.Iterator(Category.objects.all())

    class Meta:
        model = 'API.Offer'
