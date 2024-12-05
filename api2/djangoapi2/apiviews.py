from rest_framework import generics


from .models import Book, Campus
from .serializers import BookSerializer, CampusSerializer

class BooksList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class BookDetail(generics.RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CampusList(generics.ListCreateAPIView):
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer
