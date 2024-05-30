from django.urls import path
from .views import book_detail, books_list

urlpatterns = [
    path('books', books_list, name='books_list'),
    path('books/<int:pk>', book_detail, name = 'book_detail'),
]