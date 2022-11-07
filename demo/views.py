# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views import View
from .models import Book
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import BookSerializer, BookMiniSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# class Another(View):
#     books = Book.objects.all()
#     # books = Book.objects.get(id=4) 
#     # output = f'id number {books.id} and book name is {books.title}'
#     output = ''
#     for book in books:
#      output += f"We are found the {book.id} book {book.price} $ <br/>"
#     def get(self, request):
#         return HttpResponse(self.output)

# def demo(request):
#     return HttpResponse("First message from views")

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookMiniSerializer
    queryset = Book.objects.all()
    Authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    
    #I want to see whole data from specific id
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookSerializer(instance)
        return Response(serializer.data)