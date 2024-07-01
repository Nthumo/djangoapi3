from django.urls import path
from .apiviews import BooksList, BookDetail

urlpatterns = [
    path('books', BooksList.as_view(), name='books_list'),
    path('books/<int:pk>', BookDetail.as_view(), name = 'book_detail'),
]

