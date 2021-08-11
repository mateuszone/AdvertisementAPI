from random import randint

from factory.django import DjangoModelFactory
from factory.faker import Faker
from factory import Sequence, PostGenerationMethodCall, sequence, RelatedFactory, RelatedFactoryList
from factory import SubFactory

from API.models import Category


class CategoryFactory(DjangoModelFactory):
    name = Faker('word')

    @sequence
    def name(n):
        try:
            max_id = Category.objects.latest('id').id
            return f'Category-{max_id + 1}'
        except Category.DoesNotExist:
            return f'Category-0'

    class Meta:
        model = 'API.Category'


# current_category = Category.objects.last().id


class OfferFactory(DjangoModelFactory):
    title = Faker('word')
    description = Faker('paragraph')
    price = Faker('credit_card_security_code')
    # category = Faker('CategoryFactory')
    # category = RelatedFactory('API.factories.CategoryFactory', 'name', id=1)
    category = RelatedFactoryList('API.factories.CategoryFactory',
                                  'id'
                                  # size=lambda: randint(1, 5)
                                  )

    class Meta:
        model = 'API.Offer'
