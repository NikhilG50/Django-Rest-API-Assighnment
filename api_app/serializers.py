from rest_framework import serializers
from .models import Authors, Book


class Authors_serializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = '__all__'


class Book_serializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'