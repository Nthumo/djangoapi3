from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Book, Campus
from .serializers import BookSerializer

class BooksList(APIView):
    def get(self, request):
        books = Book.objects.all()[:20]
        data = BookSerializer(books, many=True).data
        return Response(data)
    
class BookDetail(APIView):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        data = BookSerializer(book).data
        return Response(data)
