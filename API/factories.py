from factory.django import DjangoModelFactory
from factory.faker import Faker
from factory import Sequence, PostGenerationMethodCall, sequence
from factory import SubFactory


class CategoryFactory(DjangoModelFactory):
    name = Faker('words')

    class Meta:
        model = 'API.Category'


class OfferFactory(DjangoModelFactory):
    title = Faker('words')
    description = Faker('paragraph')
    price = Faker('credit_card_security_code')
    category = Faker('CategoryFactory')

    class Meta:
        model = 'API.Offer'
