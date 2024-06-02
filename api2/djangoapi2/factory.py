import factory
from factory.faker import faker
from django.contrib.auth.models import User
from .models import Book, Campus

fake = faker.Faker()

class UserFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    password = factory.PostGenerationMethodCall('set_password', 'defaultpassword')




class BookFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = Book

    name = factory.Faker("sentence", nb_words=4)
    author = factory.Faker("name")
    added_by =factory.SubFactory(UserFactory)
    added_on = factory.Faker('date_time_this_year', before_now=True, after_now=False)
    book_detail = factory.Faker('sentence', nb_words=500)


class CampusFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Campus

    campus_name = factory.Faker("name")
    location = factory.Faker("sentence", nb_words=3)