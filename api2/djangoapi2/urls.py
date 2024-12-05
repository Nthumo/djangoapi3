from django.urls import path
from .apiviews import BooksList, BookDetail, CampusList

urlpatterns = [
    path('books/', BooksList.as_view(), name='books_list'),
    path('books/<int:pk>', BookDetail.as_view(), name = 'book_detail'),
    path('books/<int:pk>/campus/', CampusList.as_view(), name='campus_list'),
]

