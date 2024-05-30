from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import JsonResponse

def books_list(request):
    NUMBER = 10
    books = Book.objects.all()[:NUMBER]
    data = {'books': list(books.values('name', 'author', 'added_by__username', 'added_on', 'book_detail'))}

    return JsonResponse(data)



def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    data = {'read': {
        'added_by': book.added_by.username,
        'Book_contents': book.book_detail
    }}

    return JsonResponse(data)
