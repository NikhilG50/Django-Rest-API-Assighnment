from django.http import HttpResponse
from.models import Authors, Book
from .serializers import Authors_serializer, Book_serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def book_list(request):
    """
        Listing all the book details
    """
    if request.method == 'GET':
        book = Book.objects.all()
        serializer = Book_serializer(book, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Book_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):
    """
    Retrieve, update or delete a code Book.
    """
    try:
        bookk = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Book_serializer(bookk)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Book_serializer(bookk, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bookk.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def author_list(request):
    """
        Listing all the author details
    """
    if request.method == 'GET':
        author = Authors.objects.all()
        serializer = Authors_serializer(author, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Authors_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def author_detail(request, pk):
    """
    Retrieve, update or delete an author.
    """
    try:
        authors = Authors.objects.get(pk=pk)
    except Authors.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Authors_serializer(authors)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Authors_serializer(authors, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        authors.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
