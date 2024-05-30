import factory
from factory.faker import faker
from .models import Book

FAKE = faker.Faker()

class BookFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = Book

    name = factory.Faker("sentence", nb_words=4)
    author = factory.Faker("name")
    added_by =factory.Faker()
